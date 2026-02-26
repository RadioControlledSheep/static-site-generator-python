import os

from block_markdown import markdown_to_html_node


def extract_title(markdown):
    markdown = markdown.strip()
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("invalid markdown, no h1")


def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise ValueError(f"invalid source: {from_path}")
    if os.path.isdir(from_path):
        raise ValueError(f"invalid source: {from_path} is a directory")
    if not os.path.exists(template_path):
        raise ValueError(f"missing template: {template_path}")
    if os.path.isdir(template_path):
        raise ValueError(f"invalid template: {template_path} is a directory")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = open(from_path).read()
    title = extract_title(markdown)
    template = open(template_path).read()
    html_from_md = markdown_to_html_node(markdown).to_html()
    html = template.replace("{{ Content }}", html_from_md).replace("{{ Title }}", title)
    # print(html)
    target_file_index = dest_path.rfind("/")
    target_path = dest_path[:target_file_index]
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    with open(dest_path, "w") as f:
        f.write(html)


"""Create a generate_page(from_path, template_path, dest_path) function. It should:
Print a message like "Generating page from from_path to dest_path using template_path".
Read the markdown file at from_path and store the contents in a variable.
Read the template file at template_path and store the contents in a variable.
Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
Use the extract_title function to grab the title of the page.
Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist."""
