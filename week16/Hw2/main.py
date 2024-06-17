import requests
import re

def main():
        with open("answer.txt", "w", encoding="utf-8") as f:
            f.write("Answer")
            for i in range(1910): 
                print(i)
                url = f"https://exam.naer.edu.tw/searchResult.php?page={i}&orderBy=lastest&keyword=&selCountry=&selCategory=0&selTech=0&selYear=&selTerm=&selType=&selPublisher="
                response = requests.get(url)
                text = response.text

                t4_pattern = re.compile(r'<\w+[^>]*class=["\']?t4["\']?[^>]*>(.*?)</\w+>', re.DOTALL)

                matches = t4_pattern.finditer(text)
                for match in matches:
                    content = match.group(1)
                    patterns = [
                        re.compile(r'[^\s]+[縣市]'),
                        re.compile(r'[^\s]+國[中小]'),
                        re.compile(r'[^\s]+[領域]'),
                        re.compile(r'[^\s]+[年級]'),
                        re.compile(r'.*學期.*'),
                        re.compile(r'/otc/testStoreFile/\w+\.pdf'),
                    ]

                    for pattern in patterns:
                        match = pattern.search(content)
                        if match:
                            if '縣市' in pattern.pattern:
                                f.write("\n")
                            f.write(f"{match.group()} ")

if __name__ == "__main__":
    main()
