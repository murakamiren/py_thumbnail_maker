# path format
# base path to img name, img extension, img path removed "src/imgs", include "src/imgs" path
def path_to_img_info(img_paths):
    formatted_paths = []
    for img_path in img_paths:
        base_split_img_path = img_path.split("/")
        base_len = len(base_split_img_path)
        img_name_ex = base_split_img_path[base_len - 1]
        img_name = img_name_ex.split(".")[0]
        img_name_arr = []

        # if img_name has dot(.),join the separated str
        if len(img_name_ex.split(".")) > 2:
            for i, p in enumerate(img_name_ex.split(".")):
                if not i == len(img_name_ex.split(".")) - 1:
                    img_name_arr.append(p)
            img_name = ".".join(img_name_arr)

        # img extension
        img_ex = img_name_ex.split(".")[len(img_name_ex.split(".")) - 1]

        # format path
        # ex: "src/imgs/foo_dir/baz.jpg" to "/foo_dir/baz.jpg"
        remake_base_path_remove_src = img_path.split("src/imgs")[1]
        remake_base_path = remake_base_path_remove_src.split(".")[0]
        format_path_split = remake_base_path.split("/")
        format_path_arr = []
        for i,p in enumerate(format_path_split):
            if not i == len(format_path_split) - 1:
                format_path_arr.append(p)
        format_path = "/".join(format_path_arr)

        formatted_path = {"img_name": img_name, "img_ex": img_ex, "base_path": img_path, "format_path": format_path}
        formatted_paths.append(formatted_path)
    return formatted_paths



