from website import create_app
import os

# Set TF_ENABLE_ONEDNN_OPTS environment variable to 0
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Now you can proceed with your TensorFlow code
app = create_app()


if __name__ == '__main__':
	app.run()
