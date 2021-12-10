class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        for email in emails:
            split_email = email.split('@')
            local = split_email[0]
            domain = split_email[1]
            local = local.replace('.', '')
            split_local = local.split('+')
            local = split_local[0]
            final_email = local + '@' + domain
            if final_email not in result:
                result.append(final_email)
        return len(result)