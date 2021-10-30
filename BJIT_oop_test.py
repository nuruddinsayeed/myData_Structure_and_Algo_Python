from typing import List


class Tag:
    def __init__(self, tag) -> None:
        self.tag = tag


class WebsiteTag:
    def __init__(self, web_tag) -> None:
        self.web_tag = web_tag


class Address:
    """Address of a person"""

    def __init__(self, street, street2, city, state, country) -> None:
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.country = country


class Contact:

    def __init__(self, phone, mobile, email, fax=None):
        self.phone = phone
        self.mobile = mobile
        self.fax = fax
        self.email = email


class CustomerContactTitle:
    def __init__(self, title) -> None:
        self.title = title


class CustomerContact(Contact, CustomerContactTitle):

    def __init__(self, contact_name, title, job_position, email, phone, mobile, notes=None) -> None:
        super(CustomerContactTitle, self).__init__(title)
        super(Contact, self).__init__(phone, mobile, email)

        self.contact_name = contact_name
        self.job_position = job_position
        self.notes = notes


class Customer(Address, Contact, Tag):

    wesite_tags: List = []
    customer_contacts = []  # Customer can add multiple contacts
    inovoice_addresses = []  # Customer can add multiple invoice addresses
    shipping_addresses = []  # Customer can add multiple shipping addresses
    other_addresses = []
    # TODO :  create methods for these attrs

    def __init__(self, name, curtomer_type, language, street, street2, city, state, country, tag, phone, mobile, fax, email, website=None) -> None:
        self.name = name
        self.customer_type = curtomer_type
        self.website = website
        self.language = language
        super(Address, self).__init__(street, street2,
                                      city, state, country)
        super(Contact, self).__init__(phone, mobile, fax, email)
        super(Tag, self).__init__(tag)

    def add_website_tag(self, tag):
        self.wesite_tags.append(WebsiteTag(tag))

    def add_customer_contacts(self, contact_name, title, job_position, email, phone, mobile, notes=None):
        self.customer_contacts.append(CustomerContact(
            contact_name, title, job_position, email, phone, mobile, notes=None))

    def add_inovoice_addresses(self, street, street2, city, state, country):
        self.inovoice_addresses.append(
            Address(street, street2, city, state, country))

    def add_shipping_addresses(self, street, street2, city, state, country):
        self.shipping_addresses.append(
            Address(street, street2, city, state, country))

    def add_other_addresses(self, street, street2, city, state, country):
        self.other_addresses.append(
            Address(street, street2, city, state, country))
