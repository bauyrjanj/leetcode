def unique_email(emails):
    for i, email in enumerate(emails):
        address = email.split('@')
        local = address[0]
        domain = address[1]
        if "." in local:
            local = local.replace(".", "")
        if "+" in local:
            idx = local.index("+")
            local = local[:idx]

        emails[i] = local+'@'+domain

    return len(set(emails)), emails

if __name__=="__main__":
    # emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    # emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
    print(unique_email(emails))
    