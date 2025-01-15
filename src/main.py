import os
from shonit import Shonit
from queue import Queue
from threading import Condition
# import garuda_algorithm
from NilaSDK.logger.nila_logger import LOGGER
from NilaSDK.messaging.helpers.event_publisher import event_publisher
import configure_logger
from utils import initialize_configurations
from viewer.analyser_inference import Analyser_inference


if __name__ == '__main__':

    local_model_dir = '/Users/bhavish/NILA_Shonit'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    configure_logger.initialize_logger()
    initialize_configurations()
    LOGGER().info('Constructing Garuda-Reconstructor.....')
    garuda_algorithm.set_logger(LOGGER())
    garuda_algorithm.set_model_dir_path(local_model_dir)
    analyser_obj = Shonit(Queue(), Condition(), event_publisher(None, None))

    class Message_Data(object):
        """
        A class representing message data, this is just for simulating NAS input data(Use it only for locally testing analyser).

        Attributes:
            _data (any): The data associated with the message.
        """

        def __init__(self, data, session_data):
            self._data = data
            self._session_data = session_data

        def data(self):
            """
            Get the data associated with the message.

            Returns:
                any: The data associated with the message.
            """
            return self._data
        
        def session_data(self):
            """
            Get the session data associated with the message.

            Returns:
                any: The session data associated with the message.
            """
            return self._session_data
        
    msg_data = Message_Data(data = {
        "aoi_image":
        {
            "nx": 47,
            "ny": 51,
            "path": " stack Fov's ........ path "
        }
    },  session_data={})
    try:
        print('Recon started....')
        analyser_obj._analyse(stop_event=None, msg_data=msg_data) 
    except Exception as e:
        raise e
    finally:
        try:
            data = {
                'stack_image_path': msg_data.data()['image']['path'],
                'analysis_output_json_path': '/'.join(msg_data.data()['aoi_image']['path'].split('/')[0:-2]) + '/analyser_results/pbs.json',
                'output_path': '/'.join(msg_data.data()['aoi_image']['path'].split('/')[0:-2]) + '/debug_view' 
            } 
            data_viewer = Analyser_inference(data) 
            data_viewer.run(mark=True)
        except Exception as e:
            print(e)

            