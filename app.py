from website import create_app
import os 
os.ENVIRON["PF_ENABLE_ONEDNN_OPPS"] = "0"
app = create_app()


if __name__ == '__main__':
	app.run()
