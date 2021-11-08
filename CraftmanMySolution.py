import base64
from itertools import permutations

arr2 = [
    "56JmVudHJ5LjE5NTQwNTAzMDQ9bnVydWRkaW5zYXllZWQxNEBn",
    "b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW"
    "50cnkuMTAxMzkwOTE1PUJsck9NMkhrYmdQRzhVUDgtbnVydWRk",
    "aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU",
    "lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS",
    "aW5zYXllZWQxNCU0MGdtYWlsLmNvbS05bWNoQjRzT1JZamt6Qk",
]
end_string = "bWFpbC5jb20=="


# Decode func ---------->
def decode(string):
    base64_string = string

    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")

    return sample_string


def print_potential_urls(arr: list, end_str) -> None:
    potential_strings_lst = permutations(arr)

    for strings in potential_strings_lst:
        complete_str = "".join(strings) + end_str
        try:
            potential_url = decode(complete_str)
        except Exception as e:
            continue
        else:
            if potential_url.startswith("https://") and potential_url.endswith("nuruddinsayeed14@gmail.com"):
                print(potential_url)


print_potential_urls(arr2, end_string)
