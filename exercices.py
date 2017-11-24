import json
import elasticsearch

es = elasticsearch.Elasticsearch()
INDEX = "bd_avance"
DOC_TYPE = "emails"


def get_data(fname):
    with open(fname) as fhandle:
        for line in fhandle:
            data = json.loads(line, encoding='utf-8')
            data["id"] = data["_id"]["$oid"]  # Remapping the id for ES
            del data['_id']
            yield data


# Exercice 1.1
def index_emails(emails):
    # TODO
    pass


# Exercice 1.2
def get_email(id):
    # TODO
    pass


# Exercice 1.3
def get_email_light(id):
    # TODO
    pass


# Exercice 1.4
def get_multiple_ids(ids):
    # TODO
    pass


# Exercice 2.1
def update_email_subject(id, subject):
    # TODO
    pass


# Exercice 2.2
def delete_email(id):
    # TODO
    pass


# Exercice 3.1
def search_subject(term):
    # TODO
    pass


# Exercice 3.2
def search_emails(must, should, must_not):
    # TODO
    pass


# Exercice 3.3
def search_term_emails(must_term, must_match):
    # TODO
    pass


# Exercice 4.1
def search_subject_dsl(term):
    # TODO
    pass


# Exercice 4.2
def search_emails_dsl(must, should, must_not):
    # TODO
    pass


# Exercice 5.1
def aggregate_folders():
    # TODO
    pass


if __name__ == '__main__':
    # Things to do here
    pass
