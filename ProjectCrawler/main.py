import os
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from ebooklib import epub
from fpdf import FPDF
import threading

class LightNovelCrawler:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Novel Crawler")
        self.root.geometry("600x400")
        
        # Variables
        self.novel_url = StringVar()
        self.start_chapter = IntVar(value=1)
        self.end_chapter = IntVar(value=1)
        self.output_format = StringVar(value="epub")
        self.output_path = StringVar()
        self.status = StringVar(value="Ready")
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=BOTH, expand=True)
        
        # URL Entry
        ttk.Label(main_frame, text="Novel URL:").grid(row=0, column=0, sticky=W, pady=5)
        url_entry = ttk.Entry(main_frame, textvariable=self.novel_url, width=50)
        url_entry.grid(row=0, column=1, columnspan=2, sticky=EW, pady=5)
        
        # Chapter Range
        ttk.Label(main_frame, text="Chapter Range:").grid(row=1, column=0, sticky=W, pady=5)
        
        ttk.Label(main_frame, text="From:").grid(row=1, column=1, sticky=E, pady=5)
        start_spin = ttk.Spinbox(main_frame, from_=1, to=9999, textvariable=self.start_chapter, width=5)
        start_spin.grid(row=1, column=2, sticky=W, pady=5)
        
        ttk.Label(main_frame, text="To:").grid(row=2, column=1, sticky=E, pady=5)
        end_spin = ttk.Spinbox(main_frame, from_=1, to=9999, textvariable=self.end_chapter, width=5)
        end_spin.grid(row=2, column=2, sticky=W, pady=5)
        
        # Output Format
        ttk.Label(main_frame, text="Output Format:").grid(row=3, column=0, sticky=W, pady=5)
        format_frame = ttk.Frame(main_frame)
        format_frame.grid(row=3, column=1, columnspan=2, sticky=W)
        
        ttk.Radiobutton(format_frame, text="EPUB", variable=self.output_format, value="epub").pack(side=LEFT)
        ttk.Radiobutton(format_frame, text="PDF", variable=self.output_format, value="pdf").pack(side=LEFT, padx=10)
        
        # Output Path
        ttk.Label(main_frame, text="Output Folder:").grid(row=4, column=0, sticky=W, pady=5)
        path_entry = ttk.Entry(main_frame, textvariable=self.output_path, width=40)
        path_entry.grid(row=4, column=1, sticky=EW, pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_folder).grid(row=4, column=2, sticky=W, pady=5)
        
        # Status
        ttk.Label(main_frame, text="Status:").grid(row=5, column=0, sticky=W, pady=5)
        ttk.Label(main_frame, textvariable=self.status).grid(row=5, column=1, sticky=W, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Start Download", command=self.start_download).pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.root.quit).pack(side=LEFT, padx=5)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)
    
    def start_download(self):
        if not self.novel_url.get():
            messagebox.showerror("Error", "Please enter a novel URL")
            return
            
        if not self.output_path.get():
            messagebox.showerror("Error", "Please select an output folder")
            return
            
        if self.start_chapter.get() > self.end_chapter.get():
            messagebox.showerror("Error", "Start chapter cannot be greater than end chapter")
            return
            
        # Start download in a separate thread
        threading.Thread(target=self.download_chapters, daemon=True).start()
    
    def download_chapters(self):
        self.status.set("Downloading...")
        self.root.update()
        
        try:
            base_url = self.novel_url.get().rstrip('/')
            novel_title = self.get_novel_title(base_url)
            
            chapters = []
            for chapter_num in range(self.start_chapter.get(), self.end_chapter.get() + 1):
                chapter_url = f"{base_url}/chapter-{chapter_num}"
                chapter_content = self.get_chapter_content(chapter_url)
                
                if chapter_content:
                    chapters.append({
                        'title': f"Chapter {chapter_num}",
                        'content': chapter_content
                    })
                    self.status.set(f"Downloaded Chapter {chapter_num}")
                    self.root.update()
                else:
                    self.status.set(f"Failed to download Chapter {chapter_num}")
                    self.root.update()
            
            if not chapters:
                messagebox.showerror("Error", "No chapters were downloaded")
                self.status.set("Failed")
                return
                
            # Save the output
            output_file = os.path.join(self.output_path.get(), f"{novel_title}.{self.output_format.get()}")
            
            if self.output_format.get() == "epub":
                self.save_as_epub(novel_title, chapters, output_file)
            else:
                self.save_as_pdf(novel_title, chapters, output_file)
                
            self.status.set(f"Completed! Saved to {output_file}")
            messagebox.showinfo("Success", f"Download completed and saved to:\n{output_file}")
            
        except Exception as e:
            self.status.set("Error occurred")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def get_novel_title(self, base_url):
        try:
            response = requests.get(base_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h1', {'class': 'novel-title'}).text.strip()
            return title.replace(' ', '_').replace('/', '_')
        except Exception as e:
            return "Light_Novel"
    
    def get_chapter_content(self, chapter_url):
        try:
            response = requests.get(chapter_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the chapter container div
            chapter_container = soup.find('div', {'id': 'chapter-container'})
            
            if chapter_container:
                # Clean up the content - remove empty paragraphs and unwanted elements
                for p in chapter_container.find_all('p'):
                    if not p.text.strip():
                        p.decompose()
                
                return str(chapter_container)
            return None
        except Exception as e:
            print(f"Error fetching chapter: {str(e)}")
            return None
    
    def save_as_epub(self, title, chapters, output_file):
        book = epub.EpubBook()
        book.set_identifier('id' + title)
        book.set_title(title)
        book.set_language('en')
        
        # Add chapters
        for i, chapter in enumerate(chapters):
            chap = epub.EpubHtml(title=chapter['title'], file_name=f'chap_{i+1}.xhtml', lang='en')
            chap.content = chapter['content']
            book.add_item(chap)
            
        # Create table of contents
        book.toc = [(epub.Section(title), [chap for chap in book.get_items() if isinstance(chap, epub.EpubHtml)])]
        
        # Add navigation files
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        
        # Define spine
        book.spine = ['nav'] + [chap for chap in book.get_items() if isinstance(chap, epub.EpubHtml)]
        
        # Save the book
        epub.write_epub(output_file, book, {})
    
    def save_as_pdf(self, title, chapters, output_file):
        pdf = FPDF()
        pdf.set_title(title)
        pdf.set_author("Light Novel World")
        
        for chapter in chapters:
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Add chapter title
            pdf.cell(200, 10, txt=chapter['title'], ln=1, align='C')
            pdf.ln(10)
            
            # Add chapter content (basic text only - HTML would need more processing)
            content = BeautifulSoup(chapter['content'], 'html.parser').get_text()
            pdf.multi_cell(0, 10, txt=content)
        
        pdf.output(output_file)

if __name__ == "__main__":
    root = Tk()
    app = LightNovelCrawler(root)
    root.mainloop()