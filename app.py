from flask import Flask, request, render_template
from config import Configuration
from tz_adjustment import TimeZoneAdjustment
from notification import Notification

app = Flask(__name__)
config = Configuration()

@app.route('/')
def home():
    local_datetime = config.get_local_datetime()
    return render_template('index.html', local_datetime=local_datetime)

@app.route('/set_config', methods=['POST'])
def set_config():
    config.set_configuration(request.form['timezone'], request.form['dst_start'], request.form['dst_end'], request.form.getlist('notification_preferences'))
    return 'Configuration updated!'

@app.route('/notify')
def notify():
    notifier = Notification(config)
    notifier.send_email_notification('employee@organization.com', 'DST Update', 'DST adjustment will take place on ...')
    return 'Notification sent!'

if __name__ == '__main__':
    app.run(debug=True)