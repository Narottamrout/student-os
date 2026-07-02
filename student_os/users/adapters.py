from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied


class CollegeDomainAdapter(DefaultSocialAccountAdapter):
    ALLOWED_DOMAINS = [
        "niisgroup.org",  # confirm actual domain with admin office
        "niis.ac.in",
    ]

    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get("email")

        if not email:
            raise PermissionDenied("Email not found")

        domain = email.split("@")[-1].lower()

        if domain not in self.ALLOWED_DOMAINS:
            raise PermissionDenied(
                "Only college email accounts are allowed."
            )