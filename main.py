# 1. Test out reading and writing to markdown file
# 2.create the UI to go along in the terminal
# 3. Bash script for committing info
# Improvements: Make a UI window with tkinter and send to author of 100days ofcode, show in UI on another tab the log in a readbale format with a dropdown for each. Might need to create a database for this

from mdutils.mdutils import MdUtils
from datetime import datetime as dt
from github import Github

# Create MD file
#mdFile = MdUtils(file_name='Example_Markdown', title='Markdown File Example')
# mdFile.create_md_file()
md_file_name = "test.md"

day_no = input("What day out of 100 is this?\n")

def addingDate():
    answer = input("Is today the day you want to make an entry for? (y/n)\n")
    while True:
        if (answer.lower() == "y"):
            return dt.now().strftime("%b %d %Y")
            break
        elif(answer.lower() == "n"):
            month = input("What month is it?\n")
            day = input("What day is it?\n")
            year = input("What year is it?\n")
            return (f"{month} {day} {year}")
            break
        else:
            answer = input("Answer is invalid, please choose y/n to answer if today is the day you want to make an entry for\n")

def addProgress():
    return input("What was your progress today?\n")

def addThoughts():
    return input("What were your learnings and thoughts from today?\n")

def addLinksToWork():
    name_of_link = input("What is the name display of the link?\n")

def gitOps():
    g = Github("rishi.rkhan@gmail.com", "Mutantx12345")
    for repo in g.get_user().get_repos():
        print(repo.full_name)
    while True:
        search_string = input("What repo did you commit work to?\n")
        for repo in g.search_repositories(search_string):
            print(repo.full_name)
        answer = input("Is this repo name correct? (y/n)")
        if (answer.lower() == "y"):
            repo_name = repo.full_name
            break
        elif(answer.lower() == "n"):
            pass
        else:
            answer = input(
                "Answer is invalid, please choose y/n to answer if today is the day you want to make an entry for\n")
    repo = g.get_repo(repo_name)
    print(list(repo.get_branches()))
    while True:
        search_string = input("What branch did you commit work to?\n")
        for repo in g.sea(search_string):
            print(repo.full_name)
        answer = input("Is this repo name correct? (y/n)")
        if (answer.lower() == "y"):
            repo_name = repo.full_name
            break
        elif(answer.lower() == "n"):
            pass
        else:
            answer = input(
                "Answer is invalid, please choose y/n to answer if today is the day you want to make an entry for\n")
    return repo_full_name, repo_branch

mdFile = MdUtils(file_name=md_file_name)
mdFile.read_md_file(md_file_name)
mdFile.new_line()
mdFile.new_header(level=3, title=f"Day {day_no}: {addingDate()}",  add_table_of_contents='n')
mdFile.write(f"\n**Today's Progress**: {addProgress()}")
mdFile.write(f"\n\n**Thoughts** : {addThoughts()}")
org_repo_name, branch = gitOps()
mdFile.write(f"\n\n**Link(s) to work** \n1. [{addLinksToWork()}](https://github.com/{org_repo_name}/tree/{branch})")
mdFile.write("\n***")

# mdFile.write(text='Something')
mdFile.create_md_file()


