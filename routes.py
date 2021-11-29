import pandas as pd
import os
from flask import Flask, render_template, request, g
app = Flask(__name__)
parent_folder = '/media/jeremy/c602a316-f553-419a-859e-688208757bde/MSRVTT'
df = pd.read_csv(os.path.join(parent_folder, 'MSRVTT_JSFUSION_test.csv'))


@app.route('/', methods=['POST'])
def handle():
    if request.method == 'POST':
        if request.form.get('generate') == 'generate':
            vid = os.path.join(parent_folder, 'videos/all', df.iloc[0].video_id + '.mp4')
            return render_template('index.html', vid=vid)


if __name__ == '__main__':
    app.run(debug=True)
