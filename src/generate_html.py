import os

from block_markdown import markdown_to_html_node


def extract_title(markdown):
    markdown = markdown.strip()
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("invalid markdown, no h1")


def generate_page(from_path, template_path, dest_path, basepath="/"):
    if not os.path.exists(from_path):
        raise ValueError(f"invalid source: {from_path}")
    if os.path.isdir(from_path):
        raise ValueError(f"invalid source: {from_path} is a directory")
    if not os.path.exists(template_path):
        raise ValueError(f"missing template: {template_path}")
    if os.path.isdir(template_path):
        raise ValueError(f"invalid template: {template_path} is a directory")
    markdown = open(from_path).read()
    title = extract_title(markdown)
    template = open(template_path).read()
    html_from_md = markdown_to_html_node(markdown).to_html()
    html = (
        template.replace("{{ Content }}", html_from_md)
        .replace("{{ Title }}", title)
        .replace('href="/', f'href="{basepath}')
    )
    # print(html)
    target_file_index = dest_path.rfind("/")
    target_path = dest_path[:target_file_index]
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    if dest_path[-2:] == "md":
        dest_path = dest_path[:-2] + "html"
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(dest_path, "w") as f:
        f.write(html)


def generate_pages_recursive(
    dir_path_content, template_path, destination_dir, basepath="/"
):
    if os.path.exists(dir_path_content):
        if not os.path.exists(destination_dir):
            print(f"Creating: {destination_dir}")
            os.mkdir(destination_dir)
        listing = os.listdir(dir_path_content)
        for item in listing:
            item_path = os.path.join(dir_path_content, item)
            destination = os.path.join(destination_dir, item)
            if os.path.isfile(item_path):
                generate_page(item_path, template_path, destination)
            elif os.path.isdir(item_path):
                print(f"Entering directoy: {item_path}")
                generate_pages_recursive(
                    item_path, template_path, destination, basepath
                )
    else:
        raise ValueError("invalid source directory")
