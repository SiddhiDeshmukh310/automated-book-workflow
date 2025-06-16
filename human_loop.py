import os

# Utility to load file
def load_text(filename):
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        return ""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# Utility to save text
def save_text(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Human-in-the-loop review stage
def review_stage(stage_name, input_file, output_file):
    print(f"\n🟡 {stage_name} STAGE")
    content = load_text(input_file)
    if not content:
        print("⚠️ No content to process.")
        return
    print(f"\n--- Content from {input_file} ---\n")
    print(content)
    print("\nDo you want to (1) keep as is, or (2) edit?")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print(f"✅ Keeping content unchanged for {stage_name}.")
        save_text(output_file, content)
    elif choice == "2":
        print("✏️ Enter your edited content below (end input with a blank line):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        edited_content = "\n".join(lines)
        save_text(output_file, edited_content)
        print(f"✅ Edited content saved for {stage_name}.")
    else:
        print("⚠️ Invalid choice, skipping edit.")
        save_text(output_file, content)

# Main pipeline
if __name__ == "__main__":
    if not os.path.exists("chapter.txt"):
        print("❌ Source file 'chapter.txt' not found. Please create it first.")
        exit()

    # Review pipeline stages
    review_stage("Writer", "chapter.txt", "writer_output.txt")
    review_stage("Reviewer", "writer_output.txt", "reviewer_output.txt")
    review_stage("Editor", "reviewer_output.txt", "editor_output.txt")

    print("\n✅ Human-in-the-loop review process complete. All versions saved:")
    print(" - Writer Output: writer_output.txt")
    print(" - Reviewer Output: reviewer_output.txt")
    print(" - Editor Output: editor_output.txt")
