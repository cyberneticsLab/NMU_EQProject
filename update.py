import git

def update():
    
    my_repo = git.Repo()
    if my_repo.is_dirty(untracked_files=True):
        print('Changes detected.')


update()