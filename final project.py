"""
Resume-to-Job Match Project (Matching Edition)
---------------------------
This program uses a Tkinter GUI to compare an uploaded resume and user-defined keywords
against multiple job descriptions using OpenAI Embeddings and Cosine Similarity.
It ranks the jobs from best to worst match.
"""

# -----------------------------
# Importing Libraries
# -----------------------------
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from dotenv import load_dotenv
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings

# Load environment variables (e.g., OPENAI_API_KEY) from a .env file
load_dotenv()


class SemanticJobFinder:
    """
    The SemanticJobFinder class handles the GUI, file operations,
    and the core semantic matching logic.
    """

    def __init__(self):
        """Initialize the main application window, setup data, and widgets."""
        self.window = tk.Tk()
        self.window.title("Resume-to-Job Match Finder")
        self.window.geometry("700x600")
        self.window.resizable(False, False)

        # --- Application Variables ---
        self.resume_path = tk.StringVar()
        self.uploaded_resume_text = ""
        self.job_keyword = tk.StringVar()

        # --- Data Setup ---
        self.setup_job_data()

        # --- Initialize Embeddings ---
        try:
            # Note: This is a placeholder call. The actual embedding generation happens in find_jobs.
            # We initialize here to catch an immediate API key error.
            self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        except Exception as e:
            messagebox.showerror("API Error",
                                 f"Failed to initialize OpenAI Embeddings. Check .env file and API key: {e}")
            self.window.quit()
            return

        # Call setup function to build GUI components
        self.make_widgets()

        # Run the Tkinter main loop
        self.window.mainloop()

    # ----------------------------------------------------------
    # DATA SETUP: Hardcoded Job Descriptions
    # ----------------------------------------------------------
    def setup_job_data(self):
        """Defines all the job descriptions to compare against."""
        self.job_data = {
            "Nurse (RN)": """Providing resident-focused, high-quality care while working as a RN in post-acute facilities. Developing individualized care plans, administering medications, monitoring vital signs, and ensuring accurate documentation. Training and supervising staff as needed. Requires BSN and current state license.""",
            "Engineer (Project)": """Establish and maintain project documentation procedures for RFIs, RFCs, submittals, drawings, contracts, and correspondence. Manage document intake, tracking, approval, and distribution. Prepare daily/weekly progress reports and coordinate with resident engineers and contractors. AASHTOWare and COMPASS experience preferred.""",
            "Physical Therapist": """Provide expert outpatient physical therapy services to patients recovering from orthopedic conditions, surgeries, and injuries. Requires a Doctoral degree in Physical Therapy and an active state license. Responsibilities include treating sports injuries and musculoskeletal disorders. Dry needling a plus.""",
            "IT Support Technician": """Serve as the first line of technical assistance for a 50-person team. Focus on hardware support, equipment deployment, end-user troubleshooting, and ERP/reporting assistance. Strong Windows and Microsoft 365 skills are required. Basic networking knowledge is a must.""",
            "Chef (Line Cook)": """Experienced Line Cook to join our team. Must work quickly and efficiently, and have a strong understanding of food safety and sanitation guidelines. Passionate about cooking and committed to providing high-quality meals.""",
            "Receptionist": """First point of contact for visitors, clients, and staff, creating a welcoming and organized front-desk experience. Responsibilities include answering and directing phone calls, greeting guests, scheduling appointments, and maintaining accurate records. Strong customer service skills required."""
        }

    # ----------------------------------------------------------
    # GUI DESIGN: Widgets
    # ----------------------------------------------------------
    def make_widgets(self):
        """Constructs the GUI components using Tkinter widgets to match the screenshot."""

        # Resume Upload Section
        tk.Label(self.window, text="Upload Your Resume:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.window, textvariable=self.resume_path, width=45, state="readonly").grid(row=0, column=1, padx=5)
        tk.Button(self.window, text="Browse", command=self.upload_resume).grid(row=0, column=2, padx=5, sticky="w")

        # Job Keyword Section (User Input)
        tk.Label(self.window, text="Job Keywords/Skills:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(self.window, textvariable=self.job_keyword, width=60).grid(row=1, column=1, columnspan=2, padx=5,
                                                                            sticky="w")

        # Buttons
        ttk.Button(self.window, text="Find Jobs", command=self.find_jobs, width=15, style='Green.TButton').grid(row=2,
                                                                                                                column=1,
                                                                                                                pady=15,
                                                                                                                sticky="e")
        ttk.Button(self.window, text="Quit", command=self.window.quit, width=10, style='Red.TButton').grid(row=2,
                                                                                                           column=2,
                                                                                                           pady=15,
                                                                                                           sticky="w")

        # Configure styles for buttons
        style = ttk.Style()
        style.configure('Green.TButton', foreground='white', background='#32CD32', font=('Arial', 10, 'bold'))
        style.map('Green.TButton', background=[('active', '#228B22')])
        style.configure('Red.TButton', foreground='white', background='#FF4500', font=('Arial', 10, 'bold'))
        style.map('Red.TButton', background=[('active', '#B22222')])

        # Results Display
        tk.Label(self.window, text="Matching Job Results:", font=('Arial', 12, 'bold')).grid(row=3, column=0, padx=10,
                                                                                             pady=(10, 5), sticky="w")

        # Use Treeview to display results in a table format (like the screenshot)
        columns = ("Job Title", "Similarity Score")
        self.result_box = ttk.Treeview(self.window, columns=columns, show="headings", height=15)

        self.result_box.heading("Job Title", text="Job Title", anchor="w")
        self.result_box.heading("Similarity Score", text="Score (0.0 to 1.0)", anchor="center")

        self.result_box.column("Job Title", width=400, anchor="w")
        self.result_box.column("Similarity Score", width=150, anchor="center")

        self.result_box.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        # Status Label (to replace the "Status" button in the corner)
        self.status_var = tk.StringVar(value="Status: Ready.")
        tk.Label(self.window, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w").grid(row=5, column=0,
                                                                                               columnspan=3,
                                                                                               sticky="ew")

        # Configure weights for resizing
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(4, weight=1)

    # ----------------------------------------------------------
    # FILE HANDLING: Resume Upload
    # ----------------------------------------------------------
    def upload_resume(self):
        """Allows the user to select a resume file and reads its content."""
        try:
            file_path = filedialog.askopenfilename(
                title="Select Resume (TXT, DOCX, or PDF)",
                # Note: DOCX/PDF parsing is complex. We'll attempt a simple read,
                # but users should ideally use a PDF file for this simple example.
                filetypes=[("Print Display Format", "*.PDF"), ("All files", "*.*")]
            )
            if file_path:
                self.resume_path.set(os.path.basename(file_path))

                # Attempt to read the content as plain text
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.uploaded_resume_text = f.read()

                messagebox.showinfo("Upload Complete", f"Resume '{os.path.basename(file_path)}' loaded for matching.")
                self.status_var.set("Status: Resume loaded.")
            else:
                messagebox.showwarning("No File Selected", "Please select a resume file to continue.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file. Use a plain .txt file for best results: {e}")
            self.status_var.set("Status: File Read Error.")
            self.uploaded_resume_text = ""

    # ----------------------------------------------------------
    # CORE FUNCTIONALITY: Semantic Matching Logic
    # ----------------------------------------------------------
    def find_jobs(self):
        """
        Generates embedding for combined resume/keywords and calculates cosine similarity
        against all job descriptions, then ranks and displays results.
        """
        # --- Pre-Check Inputs ---
        if not self.uploaded_resume_text:
            messagebox.showwarning("Missing Resume", "Please upload your resume file first.")
            return

        # Clear old results
        for i in self.result_box.get_children():
            self.result_box.delete(i)
        self.status_var.set("Status: Calculating embeddings...")
        self.window.update_idletasks()

        user_keywords = self.job_keyword.get().strip()

        # --- 1. Create the Candidate Profile Document ---
        # The resume and user-entered keywords are combined to form one rich document
        candidate_profile_doc = self.uploaded_resume_text
        if user_keywords:
            candidate_profile_doc = f"{self.uploaded_resume_text}\n\nUser Keywords/Skills: {user_keywords}"

        try:
            # --- 2. Embed Candidate Profile ---
            candidate_embedding = self.embeddings.embed_query(candidate_profile_doc)
            candidate_embedding_array = np.array(candidate_embedding).reshape(1, -1)

            job_results = []

            # --- 3. Iterate, Embed Jobs, and Calculate Similarity ---
            for title, description in self.job_data.items():
                # Embed the job description
                job_embedding = self.embeddings.embed_query(description)
                job_embedding_array = np.array(job_embedding).reshape(1, -1)

                # Calculate Cosine Similarity
                similarity_score = cosine_similarity(
                    job_embedding_array,
                    candidate_embedding_array
                )[0][0]

                job_results.append((title, similarity_score))

            # --- 4. Rank Results ---
            # Sort jobs by similarity score (descending: best to worst match)
            ranked_jobs = sorted(job_results, key=lambda x: x[1], reverse=True)

            # --- 5. Display Results in Treeview ---
            for title, score in ranked_jobs:
                score_str = f"{score:.4f}"
                self.result_box.insert('', tk.END, values=(title, score_str))

            self.status_var.set(f"Status: Calculation complete. {len(ranked_jobs)} jobs ranked.")

        except Exception as e:
            messagebox.showerror("Calculation Error", f"An API or calculation error occurred:\n{e}")
            self.status_var.set("Status: ERROR occurred.")


# ----------------------------------------------------------
# MAIN PROGRAM EXECUTION
# ----------------------------------------------------------
if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        messagebox.showerror("Startup Error",
                             "The OPENAI_API_KEY environment variable is not set. Please set it in your .env file.")
    else:
        try:
            SemanticJobFinder()
        except Exception as error:
            print("An error occurred while starting the application:", error)