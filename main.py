import os

# import local files
from extract_text import extract_text
from extract_skills import extract_skills

# # download spacy model
# os.system('python -m spacy download en_core_web_sm')


def resume_parser(resume_path):
    """
    Parses resume text and extracts skills.

    Parameters
    ----------
    resume_path : str
        Path to resume file.

    Returns
    -------
    skills : list
        List of skills extracted from resume.
    """

    # extract text from resume
    extension = resume_path.split('.')[-1]
    text = extract_text(resume_path, extension)

    # extract skills from resume
    skills = extract_skills(text)

    return skills
