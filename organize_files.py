import os
import shutil

# Define the directories structure
def create_directories(base_dir):
    directories = [
        "reports",
        "subsidies",
        "visualizations"
    ]
    for dir_name in directories:
        dir_path = os.path.join(base_dir, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Directory created or already exists: {dir_path}")

# Move files to their respective folders
def move_files(base_dir):
    file_mapping = {
        "PowerBI.html": "reports",
        "enhanced_dashboard.html": "reports",
        "subsidies_heatmap_Code APE_Source Principale.html": "subsidies",
        "subsidies_heatmap_Délai_Alternative 1.html": "subsidies",
        "subsidies_heatmap_Délai_Alternative 2.html": "subsidies",
        "cost_hierarchy.html": "visualizations",
        "flux_financiers_enhanced.html": "visualizations",
        "service_hierarchy.html": "visualizations",
    }

    for file_name, folder in file_mapping.items():
        src = os.path.join(base_dir, file_name)
        dest = os.path.join(base_dir, folder, file_name)

        if os.path.exists(src):
            shutil.move(src, dest)
            print(f"Moved: {src} --> {dest}")
        else:
            print(f"File not found: {src}")

# Update file paths in HTML files
def update_html_paths(base_dir):
    html_files = [
        os.path.join(base_dir, "reports", "PowerBI.html"),
        os.path.join(base_dir, "reports", "enhanced_dashboard.html"),
        os.path.join(base_dir, "visualizations", "cost_hierarchy.html"),
        os.path.join(base_dir, "visualizations", "flux_financiers_enhanced.html"),
        os.path.join(base_dir, "visualizations", "service_hierarchy.html"),
        os.path.join(base_dir, "subsidies", "subsidies_heatmap_Code APE_Source Principale.html"),
        os.path.join(base_dir, "subsidies", "subsidies_heatmap_Délai_Alternative 1.html"),
        os.path.join(base_dir, "subsidies", "subsidies_heatmap_Délai_Alternative 2.html"),
    ]

    for html_file_path in html_files:
        if os.path.exists(html_file_path):
            with open(html_file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Update paths to point to the correct locations
            updated_content = content.replace("html_files/", "")

            with open(html_file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
                print(f"Updated paths in: {html_file_path}")

# Main function to orchestrate file organization
def main():
    base_dir = os.path.abspath("html_files")
    print("Starting organization...")
    
    # Step 1: Create directories
    create_directories(base_dir)
    
    # Step 2: Move files
    move_files(base_dir)
    
    # Step 3: Update paths
    update_html_paths(base_dir)

    print("Organization complete!")

if __name__ == "__main__":
    main()
