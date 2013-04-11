from ajax_select import make_ajax_form,admin
class Autocompletar(admin.AjaxSelectAdmin):
    class Media:
        js=("js/jquery.autocomplete.js","admin/js/ajax_select.js", "admin/js/inlines.min.js", "js/jquery-ui.min.js")
        css={"all":("admin/css/jquery.autocomplete.css","admin/css/iconic.css", "css/jquery-ui.css")}
