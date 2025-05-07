import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class SeleniumLinkExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LightNovelWorld Link Extractor (Selenium)")

        self.url_label = ttk.Label(root, text="Enter Chapters Page URL:")
        self.url_label.pack(pady=5)

        self.url_entry = ttk.Entry(root, width=80)
        self.url_entry.insert(0, "https://www.lightnovelworld.co/novel/super-god-gene-novel-05122223/chapters")
        self.url_entry.pack(pady=5)

        self.extract_button = ttk.Button(root, text="Extract Links (Selenium)", command=self.extract_links_selenium)
        self.extract_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="Extracted Links:")
        self.result_label.pack(pady=5)

        self.result_text = scrolledtext.ScrolledText(root, height=15, width=80)
        self.result_text.pack(padx=10, pady=10)
        self.result_text.config(state=tk.DISABLED)

    def extract_links_selenium(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter the chapters page URL.")
            return

        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state=tk.DISABLED)

        try:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            driver.get(url)
            time.sleep(5)

            # Save the page source for debugging
            with open("selenium_page_source.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            messagebox.showinfo("Debug", "Page source saved to selenium_page_source.html")

            chapter_list = driver.find_element(By.CSS_SELECTOR, 'ul.wp-manga-chapter-list')
            link_elements = chapter_list.find_elements(By.TAG_NAME, 'a')
            extracted_links = []
            for item in link_elements:
                href = item.get_attribute('href')
                if href and '/chapter-' in href:
                    extracted_links.append(href)
                    self.display_link(href)

            driver.quit()

            if extracted_links:
                messagebox.showinfo("Success", f"Found {len(extracted_links)} chapter links (via Selenium).")
            else:
                messagebox.showinfo("Info", "No chapter links found on this page (via Selenium).")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            
    def display_link(self, link):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.insert(tk.END, link + "\n")
        self.result_text.see(tk.END)
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.style = ttk.Style(root)
    root.style.theme_use("clam")
    app = SeleniumLinkExtractorApp(root)
    root.mainloop()