# Assetnote Wordlists

When performing security testing against an asset, it is vital to have high quality wordlists for content and subdomain discovery. This website provides you with wordlists that are up to date and effective against the most popular technologies on the internet.

Wordlists are generated on the 30th of each month, using [Commonspeak2](https://github.com/assetnote/commonspeak2/) and [GitHub Actions](https://github.com/assetnote/wordlists/actions). If there's an extension or technology that you would like a wordlist for, but it's not in the table below, [send us a PR](https://github.com/assetnote/wordlists/blob/master/.github/workflows/wordlists.yml) and it will be included on this page after the next run.

Assetnote Continuous Security automatically maps your external assets and monitors them for changes and security issues to help prevent serious breaches. If you want to protect your attack surface and would like a demonstration of our product, please reach out to us by [submitting our contact form](https://assetnote.io/#signup).

# How this repo works

On the 30th of every month, GitHub actions are used to generate wordlists using Commonspeak2. These wordlists are then committed back to the repository.

As a part of the GitHub actions, JSON files are generated using the [gen-json.py](https://github.com/assetnote/wordlists/blob/master/gen-json.py) script. These JSON files are also pushed to the repo, and then are loaded in [index.html](https://github.com/assetnote/wordlists/blob/master/index.html) using [DataTables](https://datatables.net/).

# Credits

- [cqsd](https://github.com/cqsd/daily-commonspeak2) for his initial work on automating Commonspeak2 with GitHub actions.
- [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content) for their excellent wordlists for content discovery.