import tkinter as tk
from tkinter import filedialog, messagebox

# Store uploaded files
uploaded_files = []

# Function to show the main interface
def show_main_interface():
    start_frame.pack_forget()
    main_frame.pack()

# Function to upload all documents continuously
def upload_all_documents():
    global uploaded_files
    file_paths = filedialog.askopenfilenames(
        title="Upload All Required Documents",
        filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx"), ("Text files", "*.txt")]
    )
    
    if file_paths:
        uploaded_files.extend(file_paths)
        uploaded_files_label.config(text=f"Documents Uploaded: {', '.join([path.split('/')[-1] for path in uploaded_files])}")
    else:
        uploaded_files_label.config(text="No documents uploaded.")

# Function to summarize the case
def summarize_case():
    if selected_case_var.get() not in cases or selected_case_var.get() == "Select a Case":
        messagebox.showwarning("Warning", "Please select a case to summarize.")
        return
    case_details = cases[selected_case_var.get()]["details"]
    messagebox.showinfo("Case Summary", f"Case Summary:\n{case_details}")

# Function to update case selection
def on_case_selected(*args):
    selected_case = selected_case_var.get()
    if selected_case == "Add New Case":
        add_new_case()
    elif selected_case != "Select a Case":
        case_dropdown.pack_forget()
        case_label.pack_forget()
        case_details_label.config(text=cases[selected_case]["details"])
        case_details_label.pack(pady=5)
        instruction_label.pack(pady=5)
        upload_button.pack(pady=10)
        summarize_button.pack(pady=10)
        confirm_button.pack(pady=10)
        back_button.pack(pady=5)
        uploaded_files_label.pack(pady=5)
    else:
        case_details_label.pack_forget()
        instruction_label.pack_forget()
        upload_button.pack_forget()
        summarize_button.pack_forget()
        confirm_button.pack_forget()
        back_button.pack_forget()
        uploaded_files_label.pack_forget()

# Function to add a new case
def add_new_case():
    new_case_window = tk.Toplevel(root)
    new_case_window.title("Add New Case")
    new_case_window.geometry("300x250")
    
    tk.Label(new_case_window, text="Case Number:").pack(pady=5)
    case_number_entry = tk.Entry(new_case_window, width=30)
    case_number_entry.pack(pady=5)
    
    tk.Label(new_case_window, text="First Name:").pack(pady=5)
    first_name_entry = tk.Entry(new_case_window, width=30)
    first_name_entry.pack(pady=5)
    
    tk.Label(new_case_window, text="Last Name:").pack(pady=5)
    last_name_entry = tk.Entry(new_case_window, width=30)
    last_name_entry.pack(pady=5)
    
    def submit_new_case():
        case_number = case_number_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        
        if case_number and first_name and last_name:
            case_key = f"Case {case_number}"
            cases[case_key] = {
                "first_name": first_name,
                "last_name": last_name,
                "details": f"{first_name} {last_name} - Case {case_number}",
                "case_number": case_number
            }
            update_case_dropdown()
            selected_case_var.set(case_key)
            on_case_selected()
            new_case_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Please fill in all the details.")

    tk.Button(new_case_window, text="Submit", command=submit_new_case).pack(pady=10)

# Function to update the case dropdown options
def update_case_dropdown():
    menu = case_dropdown["menu"]
    menu.delete(0, "end")
    for case in cases.keys():
        menu.add_command(label=case, command=lambda value=case: selected_case_var.set(value))
    menu.add_command(label="Add New Case", command=lambda: selected_case_var.set("Add New Case"))

# Function to confirm document upload
def confirm_upload():
    if uploaded_files:
        messagebox.showinfo("Confirmation", "All documents are uploaded and confirmed.")
    else:
        messagebox.showwarning("Warning", "No documents have been uploaded.")

# Function to go back to the case menu
def go_back_to_case_menu():
    case_details_label.pack_forget()
    instruction_label.pack_forget()
    upload_button.pack_forget()
    summarize_button.pack_forget()
    confirm_button.pack_forget()
    back_button.pack_forget()
    uploaded_files_label.pack_forget()
    case_dropdown.pack(pady=10)
    case_label.pack(pady=5)

# Create main window
root = tk.Tk()
root.title("Divorce Settlement Case Manager")
root.geometry("500x500")

# Start screen frame
start_frame = tk.Frame(root)
tk.Label(start_frame, text="DIVORCE CASE MANAGEMENT", font=("Arial", 16)).pack(pady=20)
tk.Button(start_frame, text="Start", command=show_main_interface).pack(pady=20)
start_frame.pack()

# Main interface frame
main_frame = tk.Frame(root)
instructions_label = tk.Label(main_frame, text="Select a Divorce Case and Upload Required Documents", font=("Arial", 14))
instructions_label.pack(pady=20)

case_label = tk.Label(main_frame, text="Please select a divorce case from the dropdown menu", font=("Arial", 12))
case_label.pack(pady=5)

cases = {"Select a Case": {"first_name": "", "last_name": "", "details": "", "case_number": ""}}

selected_case_var = tk.StringVar()
selected_case_var.set("Select a Case")
case_dropdown = tk.OptionMenu(main_frame, selected_case_var, *cases.keys())
case_dropdown.pack(pady=10)
selected_case_var.trace("w", on_case_selected)
update_case_dropdown()

case_details_label = tk.Label(main_frame, text="Case details will appear here", font=("Arial", 10))
instruction_label = tk.Label(main_frame, text="Upload the required documents. Required documents in BC include:\n1. Marriage Certificate\n2. Separation Agreement (if applicable)\n3. Financial Statements\n4. Child Support Documentation\n5. Property Division Documents\n6. Spousal Support Documentation\n7. Any Other Relevant Court Forms\n\nYou may select multiple files at once.", justify="left")

upload_button = tk.Button(main_frame, text="Upload All Required Documents", command=upload_all_documents)
summarize_button = tk.Button(main_frame, text="Summarize Case", command=summarize_case)
uploaded_files_label = tk.Label(main_frame, text="Uploaded Files: None")
confirm_button = tk.Button(main_frame, text="Confirm Upload", command=confirm_upload)
back_button = tk.Button(main_frame, text="Back to Case Menu", command=go_back_to_case_menu)

main_frame.pack_forget()

root.mainloop()



