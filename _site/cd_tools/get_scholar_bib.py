from scholarly import scholarly
import re
import requests

def format_authors_bibtex_style(author_str):
    authors = author_str.split(' and ')
    formatted = []
    for name in authors:
        parts = name.strip().split()
        if len(parts) >= 2:
            last = parts[-1]
            first = ' '.join(parts[:-1])
            formatted.append(f"{last}, {first}")
        else:
            formatted.append(name)  # fallback for malformed name
    return ' and '.join(formatted)


def extract_journal_name(citation):
    # Match from start until just before the volume (assumes volume starts with a number)
    match = re.match(r'^(.+?)\s\d+\s*\(', citation)
    if match:
        return match.group(1).strip()
    else:
        return citation.strip()  # fallback


def capitalize_journal_name(name):

    lowercase_words = {"of", "and", "the", "an", "in", "on", "for", "to", "by", "as", "npj"}
    special_case = ['npj']

    # Split the name into words
    words = name.split()
    
    # Capitalize each word unless it's in the lowercase list, unless it's the first word (except for special cases)
    capitalized_words = [
        word if word.lower() in special_case else (word.capitalize() if (i == 0 or word.lower() not in lowercase_words) else word.lower())
        for i, word in enumerate(words)
    ]
    
    # Join the words back together into a string
    return " ".join(capitalized_words)


def main():

    journal_abbreviations = {
        "Nature Communications": "Nat. Commun.",
        "Wiley Interdisciplinary Reviews: Computational Molecular Science": "Wiley Inter. Rev.",
        "npj Computational Materials": "npj Comput. Mater.",
        "The Journal of Physical Chemistry Letters": "JPCL",
        "Science China Technological Sciences": "SCTS",
        "Electrochimica Acta": "Electrochim. Acta",
        "Science Bulletin": "Sci. Bull.",
        "Foundations of Data Science": "FoDS",
        "Nature Machine Intelligence": "Nat. Mach. Intell.",
        "Journal of Materials Chemistry A": "JMCA",
        "Journal of Chemical Theory and Computation": "JCTC",
        "Journal of Chemical Information and Modeling": "JCIM",
        "Small": "Small",
        "Chinese Journal of Structural Chemistry": "CJSC",
        "Journal of Computational Biophysics and Chemistry": "JCBC",
        "The Journal of Physical Chemistry A": "JPCA",
        "Computational and Mathematical Biophysics": "CMB",
        "arxiv": "ArXiv"
    }

    # Scholar ID
    scholar_id = "BJ1-8aEAAAAJ"
    author = scholarly.search_author_id(scholar_id)
    author_filled = scholarly.fill(author, sections=["publications"])

    # Write BibTeX file
    exist_journal = []
    with open("manual_bibtex.bib", "w", encoding='utf-8') as f:
        for i, pub in enumerate(author_filled['publications']):
            pub_filled = scholarly.fill(pub)

            # Get information ###################################################
            bib = pub_filled.get("bib", {})

            title = bib.get("title", "No title")
            author = bib.get("author", "Unknown")
            year = bib.get("pub_year", "Unknown")
            publisher = bib.get("publisher", "")
            if 'journal' in bib:
                journal = bib.get("journal", "")
            elif 'citation' in bib:
                journal = extract_journal_name(bib['citation'])
            else:
                journal = ""
            journal = capitalize_journal_name(journal)
            entry_type = "article" if journal else "misc"

            if 'arxiv' in journal.lower():
                abbr = 'ArXiv'
            elif 'Foundations of Data Science' in journal:
                abbr = 'FoDS'
            elif journal in journal_abbreviations:
                abbr = journal_abbreviations[journal]
            else:
                abbr = ""

            if journal not in exist_journal:
                exist_journal.append(journal)

            number = bib.get('number', "")
            pages = bib.get('pages', "")
            volume = bib.get('volume', "")
            pub_url = pub_filled.get('pub_url', "")

            # Generate a BibTeX key
            first_author_full = author.split(" and ")[0]
            last_name = first_author_full.strip().split()[-1].lower()
            first_title_word = title.split()[0].lower()
            bibkey = f"{last_name}{year}{first_title_word}"

            bibtex_entry = f"@{entry_type}{{{bibkey},\n" \
                        f"  title={{{title}}},\n" \
                        f"  author={{{format_authors_bibtex_style(author)}}},\n" \
                        f"  year={{{year}}},\n"

            if journal:
                bibtex_entry += f"  journal={{{journal}}},\n"
            if volume:
                bibtex_entry += f"  volume={{{volume}}},\n"
            if pages:
                bibtex_entry += f"  pages={{{pages}}},\n"
            if pub_url:
                bibtex_entry += f"  url={{{pub_url}}},\n"
            if publisher:
                bibtex_entry += f"  publisher={{{publisher}}},\n"
            if abbr:
                bibtex_entry += f"  abbr={{{abbr}}},\n"

            bibtex_entry += "}\n"

            # write in file ####################################################
            f.write(bibtex_entry + "\n")
            # print(i)
            # if i > 2:
            #     break
    return None


if __name__ == "__main__":
    main()
