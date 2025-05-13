import sys

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

# The content of this string is evaluated by Jinja, and plays an important role.
# It updates the djinit context to trim leading and trailing spaces
# from domain/email values
"""
{{ djinit.update({ "domain_name": djinit.domain_name | trim }) }}
{{ djinit.update({ "email": djinit.email | trim }) }}
"""

project_slug = "{{ djinit.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert project_slug.isidentifier(), "'{}' project slug is not a valid Python identifier.".format(project_slug)

assert project_slug == project_slug.lower(), "'{}' project slug should be all lowercase".format(project_slug)

assert "\\" not in "{{ djinit.author_name }}", "Don't include backslashes in author name."

if "{{ djinit.use_whitenoise }}".lower() == "n" and "{{ djinit.cloud_provider }}" == "None":
    print("You should either use Whitenoise or select a Cloud Provider to serve static files")
    sys.exit(1)

if "{{ djinit.mail_service }}" == "Amazon SES" and "{{ djinit.cloud_provider }}" != "AWS":
    print("You should either use AWS or select a different Mail Service for sending emails.")
    sys.exit(1)
