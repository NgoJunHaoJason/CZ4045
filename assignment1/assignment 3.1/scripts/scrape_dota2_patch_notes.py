'''
Script for scraping dota 2 patch notes from http://www.dota2.com/patches/.
This works as of 1 October 2020.
'''
from bs4 import BeautifulSoup
import requests
import os


# make sure we are in the right directory
os.chdir(os.path.dirname(os.path.dirname(__file__)))
print(f'current dir: {os.getcwd()}')

txt_dir_path = os.path.join(os.getcwd(), 'data/dota2/')
os.makedirs(txt_dir_path, exist_ok=True)  # set-up directory for data

# get the latest 20 patch version numbers first
base_url = 'http://www.dota2.com/patches/'
response = requests.get(base_url)

if response.status_code != 200:
    print('something went wrong')
    quit()

raw_html = response.text
soup = BeautifulSoup(raw_html, 'html.parser')

body = soup.body
patch_picker = body.find('div', attrs={'class': 'PatchPicker'})

patch_options = patch_picker.find_all('option')
latest_20_versions = [
    patch_option.string
    for patch_option in patch_options[1:21]  # ignore 'Select an update...'
]
print(latest_20_versions)

# get patch note for each version
for version in latest_20_versions:
    print(f'working on version {version}')

    url = base_url + version
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Request failed for {url}')
        continue

    raw_html = response.text
    soup = BeautifulSoup(raw_html, 'html.parser')

    body = soup.body
    main_contents = body.find('div', attrs={'class': 'MainContents'})

    # save data to this txt file
    txt_file_path = os.path.join(txt_dir_path, version + '.txt')
    with open(txt_file_path, mode='w') as txt_file:

        # the following code gets general patch notes
        general_section = main_contents.find('div', attrs={'id': 'GeneralSection'})

        if general_section is not None:
            general_header = general_section.find('p', attrs={'class': 'SectionHeader'})
            txt_file.write(general_header.string.strip() + '\n')

            patch_notes = general_section.find_all('li', attrs={'class': 'PatchNote'})

            for patch_note in patch_notes:
                if patch_note.string is None:
                    continue

                # remove starting new-line
                patch_note_string = patch_note.string.strip()
                txt_file.write('\t' + patch_note_string + '\n')

            txt_file.write('\n')  # spacing

        # the following code gets patch notes for items
        items_section = main_contents.find('div', attrs={'id': 'ItemsSection'})

        if items_section is not None:
            items_header = items_section.find('p', attrs={'class': 'SectionHeader'})
            txt_file.write(items_header.string.strip() + '\n')

            item_notes = items_section.find_all('div', attrs={'class': 'ItemNotes'})

            for item_note in item_notes:
                item_name = item_note.find('div', attrs={'class': 'ItemName'})
                txt_file.write(item_name.string.strip() + '\n')

                patch_notes = item_note.find_all('li', attrs={'class': 'PatchNote'})

                for patch_note in patch_notes:
                    if patch_note.string is None:
                        continue
                    # remove starting new-line
                    patch_note_string = patch_note.string.strip()
                    txt_file.write('\t' + patch_note_string + '\n')

                txt_file.write('\n')  # spacing

        # the following code gets patch notes for heroes
        # there 3 main types of notes for each hero (each is optional):
        # 1. general notes
        # 2. notes for hero's abilities
        # 3. notes for hero's talents
        heroes_section = main_contents.find('div', attrs={'id': 'HeroesSection'})

        if heroes_section is not None:
            heroes_header = heroes_section.find('p', attrs={'class': 'SectionHeader'})
            txt_file.write(heroes_header.string.strip() + '\n')

            hero_notes = heroes_section.find_all('div', attrs={'class': 'HeroNotes'})

            for hero_note in hero_notes:
                hero_name = hero_note.find('div', attrs={'class': 'HeroName'})
                txt_file.write(hero_name.string.strip() + '\n')

                # the following code gets general notes for this hero
                hero_notes_list = hero_note.find('ul', attrs={'class': 'HeroNotesList'})
                if hero_notes_list is not None:
                    patch_notes = hero_notes_list.find_all('li', attrs={'class': 'PatchNote'})

                    for patch_note in patch_notes:
                        if patch_note.string is None:
                            continue

                        # remove starting new-line
                        patch_note_string = patch_note.string.strip()
                        txt_file.write('\t' + patch_note_string + '\n')

                # the following code gets ability notes for this hero
                hero_abilities = hero_note.find('div', attrs={'class': 'HeroAbilities'})
                if hero_abilities is not None:
                    hero_ability_notes = hero_abilities.find_all('div', attrs={
                        'class': 'HeroAbilityNotes',
                    })

                    for hero_ability_note in hero_ability_notes:
                        ability_name = hero_ability_note.find('div', attrs={'class': 'AbilityName'})
                        txt_file.write('\t' + ability_name.string.strip() + '\n')

                        patch_notes = hero_ability_note.find_all('li', attrs={'class': 'PatchNote'})

                        for patch_note in patch_notes:
                            if patch_note.string is None:
                                continue
                            # replace starting new-line with tab for nicer format
                            patch_note_string = patch_note.string.strip()
                            txt_file.write('\t\t' + patch_note_string + '\n')

                # the following code gets talent notes for this hero
                talent_notes = hero_note.find('div', attrs={'class': 'TalentNotes'})
                if talent_notes is not None:
                    talents_label = talent_notes.find('div', attrs={'class': 'TalentsLabel'})
                    txt_file.write('\t' + talents_label.string.strip() + '\n')

                    patch_notes = talent_notes.find_all('li', attrs={'class': 'PatchNote'})

                    for patch_note in patch_notes:
                        if patch_note.string is None:
                            continue
                        # replace starting new-line with tab for nicer format
                        patch_note_string = patch_note.string.strip()
                        txt_file.write('\t\t' + patch_note_string + '\n')

                txt_file.write('\n')  # spacing

print('done')
