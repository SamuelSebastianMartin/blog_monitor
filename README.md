# Blog Monitor

### In development

## Aim

To build a module that will monitor students' journal entries, and examine them for signs of stress, unhappiness and problems.

## Process

Not having access to the Moodle API, the journal must be downloaded via the front door, using `download_blog.py`.
The text will then be analysed against a list of trigger words, using `analyse_posts.py`
Finally, it will send an alert of any flagged posts by email or SMS.

## To Do

- Build `analyse_posts.py` & `send_alert.py`
- Use *NLTK* language processing to deepen sensitivity of `analyse_posts.py`.
- Set Firefox profile in *Selenium Driver* to download to CWD.

## Problems

- *Moodle Forum* does not permit export unless *Portfolios* are enabled, which is not the case at my university. This is possible with *Moodlerooms Forum*, but unfortunately my students' journals are all in *Moodle Forum*. For this reason, the current development stage of this project is slightly fragmented: the journals exported by `download_blog.py` are actually not their journals, but some other posts. This will continue until the end of the academic year. Consequently, any text data analysed is not genuine and is sourced from elsewhere, and so alert mechanisms will not be used (or written?) until then.
- *Selenium* cannot handle pop-up windows, so `download_blog.py` uses a specific *Firefox* profile set to save all downloads to *Desktop*. This causes extra complexity in identifying and moving the downloaded file before processing.
