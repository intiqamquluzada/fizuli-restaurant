class Uploader:

    @staticmethod
    def upload_photo_for_about(instance, filename):
        return f"about/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_personal(instance, filename):
        return f"personal/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_catering(instance, filename):
        return f"catering/{filename}"

    @staticmethod
    def upload_photo_for_icon(instance, filename):
        return f"icon/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_menu(instance, filename):
        return f"menu/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_home_header(instance, filename):
        return f"homeHeader/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_logo(instance, filename):
        return f"logo/{instance.slug}/{filename}"
    
    