import falcon
from falcon_multipart.middleware import MultipartMiddleware

from config import configuration
configuration()
from views import RecognitionView, LabelsView, RecognitionOldView

api = application = falcon.API(middleware=[MultipartMiddleware()])

recognition_view = RecognitionView()
api.add_route('/api/v2/recognition', recognition_view)
labels_view = LabelsView()
api.add_route('/api/v1/labels', labels_view)
recognition_old_view = RecognitionOldView()
api.add_route('/api/v1/recognition', recognition_old_view)
