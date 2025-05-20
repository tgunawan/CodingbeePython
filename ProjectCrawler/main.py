import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

from xhtml2pdf import pisa
from io import BytesIO

from ebooklib import epub
from bs4 import BeautifulSoup

class NovelCrawlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Novel Crawler & Converter")

        self.url_label = ttk.Label(root, text="Enter Novel Main Page URL:")
        self.url_label.pack(pady=5)

        self.url_entry = ttk.Entry(root, width=80)
        self.url_entry.insert(0, "https://novelbin.com/b/a-hundredfold-training-system-instantly-upgrades-999")
        self.url_entry.pack(pady=5)

        self.start_chapter_label = ttk.Label(root, text="Start Chapter (optional, e.g., 1 or leave blank for first):")
        self.start_chapter_label.pack(pady=5)
        self.start_chapter_entry = ttk.Entry(root, width=20)
        self.start_chapter_entry.pack(pady=5)

        self.end_chapter_label = ttk.Label(root, text="End Chapter (optional, e.g., 10 or leave blank for last):")
        self.end_chapter_label.pack(pady=5)
        self.end_chapter_entry = ttk.Entry(root, width=20)
        self.end_chapter_entry.pack(pady=5)

        self.crawl_button = ttk.Button(root, text="Crawl Novel", command=self.start_crawling)
        self.crawl_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="Progress/Output:")
        self.result_label.pack(pady=5)

        self.result_text = scrolledtext.ScrolledText(root, height=15, width=80)
        self.result_text.pack(padx=10, pady=10)
        self.result_text.config(state=tk.DISABLED)

        self.novel_content = []

    def update_progress(self, message):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.insert(tk.END, message + "\n")
        self.result_text.see(tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def start_crawling(self):
        main_novel_url = self.url_entry.get().strip()
        start_chapter_input = self.start_chapter_entry.get().strip()
        end_chapter_input = self.end_chapter_entry.get().strip()

        if not main_novel_url:
            messagebox.showerror("Error", "Please enter the main novel page URL.")
            return

        start_chapter = int(start_chapter_input) if start_chapter_input.isdigit() else None
        end_chapter = int(end_chapter_input) if end_chapter_input.isdigit() else None

        self.novel_content = []
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.update_progress("Starting novel crawling...")

        driver = None
        try:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
            service = ChromeService(ChromeDriverManager().install()) # Removed log_level
            driver = webdriver.Chrome(service=service, options=chrome_options)

            self.update_progress(f"Navigating to main novel page: {main_novel_url}")
            driver.get(main_novel_url)
            time.sleep(3)

            self.update_progress("Clicking 'Chapter List' tab...")
            try:
                chapter_list_tab = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[text()="Chapter List" or @href="#tab-chapters"]'))
                )
                driver.execute_script("arguments[0].scrollIntoView();", chapter_list_tab)
                chapter_list_tab.click()
                self.update_progress("Clicked 'Chapter List' tab. Waiting for content to load...")
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#tab-chapters.tab-pane.active'))
                )
                time.sleep(2)
            except Exception as e:
                messagebox.showerror("Error", f"Could not click 'Chapter List' tab or wait for its content: {e}")
                driver.quit()
                return

            self.update_progress("Checking for 'Load more' button...")
            while True:
                try:
                    # Use a slightly longer wait for the button as it's a dynamic element
                    load_more_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Load more")]'))
                    )
                    driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
                    load_more_button.click()
                    self.update_progress("Clicked 'Load more' button...")
                    
                    # --- CRITICAL: Wait for new chapters to load after clicking "Load more" ---
                    # We need to wait for the number of chapter links to increase
                    # Get the initial count before clicking "Load more"
                    initial_chapter_count = len(driver.find_elements(By.CSS_SELECTOR, 'div#tab-chapters ul.list-chapters li a'))
                    
                    # Wait until the number of chapter elements is greater than the initial count
                    WebDriverWait(driver, 15).until( # Increased wait time
                        lambda d: len(d.find_elements(By.CSS_SELECTOR, 'div#tab-chapters ul.list-chapters li a')) > initial_chapter_count
                    )
                    time.sleep(1) # Give a brief moment for rendering
                    # --- END CRITICAL CHANGE ---

                except Exception:
                    self.update_progress("No more 'Load more' button found or all chapters loaded.")
                    break

            self.update_progress("Extracting chapter links...")
            chapter_links = []
            try:
                # Now that we've waited for all potential chapters to load, get the final list
                chapter_elements = driver.find_elements(By.CSS_SELECTOR, 'div#tab-chapters ul.list-chapters li a')
                for element in chapter_elements:
                    href = element.get_attribute('href')
                    if href and '/chapter-' in href: # Ensure it's a valid chapter link
                        chapter_links.append(href)
            except Exception as e:
                messagebox.showerror("Error", f"Could not find chapter list elements after tab click: {e}")
                driver.quit()
                return

            if not chapter_links:
                messagebox.showinfo("Info", "No chapter links found on this page after clicking tab.")
                driver.quit()
                return

            self.update_progress(f"Found {len(chapter_links)} potential chapter links.")
            chapter_links = sorted(list(set(chapter_links)))

            filtered_chapter_links = []
            for link in chapter_links:
                try:
                    chapter_number_str = link.split('/chapter-')[-1].split('-')[0]
                    chapter_number = int(chapter_number_str)
                    
                    if (start_chapter is None or chapter_number >= start_chapter) and \
                       (end_chapter is None or chapter_number <= end_chapter):
                        filtered_chapter_links.append(link)
                except ValueError:
                    continue
            
            chapter_links = filtered_chapter_links
            self.update_progress(f"Filtered to {len(chapter_links)} chapters based on input range.")

            if not chapter_links:
                messagebox.showinfo("Info", "No chapters found within the specified range.")
                driver.quit()
                return

            for i, chapter_url in enumerate(chapter_links):
                self.update_progress(f"Scraping chapter {i+1}/{len(chapter_links)}: {chapter_url}")
                chapter_data = self.scrape_chapter_content(driver, chapter_url)
                if chapter_data:
                    self.novel_content.append(chapter_data)
                time.sleep(0.5)

            # Get novel title from the main page after all other operations
            novel_title = "Novel Scraped" # Default
            try:
                # Re-navigate to the main novel URL to ensure we can get the title
                driver.get(main_novel_url)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.novel-info h1'))
                )
                novel_title_element = driver.find_element(By.CSS_SELECTOR, 'div.novel-info h1')
                novel_title = novel_title_element.text.strip() if novel_title_element else "Novel Scraped"
            except Exception as e:
                self.update_progress(f"Could not get novel title from main page: {e}. Using default.")
            
            # Ensure the title is safe for filenames
            novel_title_safe = "".join([c for c in novel_title if c.isalnum() or c in (' ', '-', '_')]).rstrip()
            if not novel_title_safe:
                novel_title_safe = "NovelScraped"


            self.update_progress("Finished scraping all chapters.")

            if self.novel_content:
                self.update_progress("Converting to PDF...")
                self.convert_to_pdf(self.novel_content, f"{novel_title_safe}.pdf")
                self.update_progress("Converting to EPUB...")
                self.convert_to_epub(self.novel_content, f"{novel_title_safe}.epub")
                messagebox.showinfo("Success", "Novel successfully crawled and converted!")
            else:
                messagebox.showinfo("Info", "No content was scraped to convert.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during crawling: {e}")
            self.update_progress(f"Error: {e}")
        finally:
            if driver:
                driver.quit()

    def scrape_chapter_content(self, driver, chapter_url):
        try:
            driver.get(chapter_url)
            time.sleep(2)

            chapter_title = ""
            try:
                # Based on image_d2c8c7.png, the chapter title is indeed within h3 inside chr-content.
                title_element = driver.find_element(By.CSS_SELECTOR, '#chr-content h3') #
                chapter_title = title_element.text.strip()
            except Exception:
                self.update_progress(f"Warning: Could not find specific h3 title for {chapter_url}. Trying general h1/h2.")
                try:
                    title_element = driver.find_element(By.CSS_SELECTOR, 'h1, h2')
                    chapter_title = title_element.text.strip()
                except Exception:
                    self.update_progress(f"Warning: Could not find any suitable title for {chapter_url}")
                    chapter_title = "Untitled Chapter"

            content_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'chr-content'))
            )

            # Based on image_d2c8c7.png, content is directly in <p> tags within chr-content.
            # We need to filter out script tags and specific divs that are not content.
            paragraphs = content_div.find_elements(By.XPATH, './/p[not(ancestor::div[contains(@class, "ads") or contains(@class, "hidden") or contains(@class, "chapter-ad") or contains(@class, "content-wrapper") or contains(@class, "container") or contains(@class, "speechify-embedded-player")]) and not(ancestor::script)]') #
            
            chapter_text = ""
            for p_tag in paragraphs:
                text = p_tag.text.strip()
                if text:
                    chapter_text += text + "\n\n"

            return {"title": chapter_title, "content": chapter_text}

        except Exception as e:
            self.update_progress(f"Error scraping {chapter_url}: {e}")
            return None

    def convert_to_pdf(self, novel_data, output_filename):
        # Create a single HTML string from all chapters
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Novel</title>
            <style>
                body { font-family: sans-serif; margin: 2cm; }
                h1 { text-align: center; margin-bottom: 1cm; }
                h2 { page-break-before: always; margin-top: 1cm; margin-bottom: 0.5cm; }
                p { text-align: justify; margin-bottom: 0.5cm; }
            </style>
        </head>
        <body>
        """
        
        novel_title = "Novel Scraped"
        if novel_data:
            first_chapter_title = novel_data[0]['title']
            if ' - Chapter ' in first_chapter_title:
                novel_title = first_chapter_title.split(' - Chapter ')[0].strip()
            elif 'Chapter ' in first_chapter_title:
                 novel_title = first_chapter_title.split('Chapter ')[0].strip()
            else:
                novel_title = "Scraped Novel"

        html_content += f"<h1>{novel_title}</h1>\n"

        for chapter in novel_data:
            clean_title = chapter['title'].replace('\xa0', ' ').replace('\u200b', '')
            clean_content = chapter['content'].replace('\xa0', ' ').replace('\u200b', '')
            
            html_paragraphs = "".join([f"<p>{p.strip()}</p>\n" for p in clean_content.split('\n\n') if p.strip()])

            html_content += f"<h2>{clean_title}</h2>\n{html_paragraphs}"

        html_content += """
        </body>
        </html>
        """

        try:
            result_file = open(output_filename, "w+b")
            
            pisa_status = pisa.CreatePDF(
                html_content,
                dest=result_file)
            
            result_file.close()
            
            if not pisa_status.err:
                self.update_progress(f"PDF saved as {output_filename}")
            else:
                self.update_progress(f"Error saving PDF: {pisa_status.err}")
                messagebox.showerror("PDF Error", f"An error occurred during PDF conversion: {pisa_status.err}")

        except Exception as e:
            self.update_progress(f"Error saving PDF: {e}")
            messagebox.showerror("PDF Error", f"An unexpected error occurred during PDF conversion: {e}")


    def convert_to_epub(self, novel_data, output_filename):
        book = epub.EpubBook()

        novel_title = "Scraped Novel"
        if novel_data:
            first_chapter_title = novel_data[0]['title']
            if ' - Chapter ' in first_chapter_title:
                novel_title = first_chapter_title.split(' - Chapter ')[0].strip()
            elif 'Chapter ' in first_chapter_title:
                novel_title = first_chapter_title.split('Chapter ')[0].strip()
            else:
                novel_title = "Scraped Novel"

        book.set_identifier(novel_title.replace(" ", "-").lower())
        book.set_title(novel_title)
        book.set_language('en')
        book.add_author('Scraped Content')

        chapters = []
        for i, chapter_data in enumerate(novel_data):
            title = chapter_data['title']
            content = chapter_data['content']

            c = epub.EpubHtml(title=title, file_name=f'chap_{i+1}.xhtml', lang='en')
            
            soup = BeautifulSoup(features="html.parser")
            body_tag = soup.new_tag("body")
            
            h2_tag = soup.new_tag("h2")
            h2_tag.string = title
            body_tag.append(h2_tag)
            
            for paragraph_text in content.split('\n\n'):
                if paragraph_text.strip():
                    p_tag = soup.new_tag("p")
                    clean_paragraph = paragraph_text.strip().replace('\xa0', ' ').replace('\u200b', '')
                    p_tag.string = clean_paragraph
                    body_tag.append(p_tag)
            
            c.content = str(body_tag)
            
            book.add_item(c)
            chapters.append(c)

        book.toc = tuple(chapters)
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        book.spine = ['nav'] + chapters

        try:
            epub.write_epub(output_filename, book, {})
            self.update_progress(f"EPUB saved as {output_filename}")
        except Exception as e:
            self.update_progress(f"Error saving EPUB: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.style = ttk.Style(root)
    root.style.theme_use("clam")
    app = NovelCrawlerApp(root)
    root.mainloop()