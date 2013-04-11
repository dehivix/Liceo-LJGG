
class ReportarErrorMiddleware(object):
  def process_exception(self, request, exception):
        """
        Add user details.
        """
        request.META['USER'] = request.user
