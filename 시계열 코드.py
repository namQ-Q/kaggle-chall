# 남규 :

#!pip install dash dash-core-components dash-html-components plotly pandas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import plotly.express as px
import plotly.graph_objects as go



# 대쉬보드 이용해서 시각화하기=============================================================================================

gsheet_url = "https://docs.google.com/spreadsheets/d/1McH-oBzPZ8ewfyEl605wq-9b3gZHCIIBVbWHEHwNnIs/gviz/tq?tqx=out:csv&sheet=ames-spot"

hot_spot= pd.read_csv(gsheet_url)

house = pd.read_csv('data/house_loc.csv')
house.rename(columns={'Unnamed: 0': 'Id'}, inplace=True)

fig = go.Figure(go.Scattermapbox(
  lat = hot_spot['Latitude'], lon = hot_spot['Longitude'],
  mode = 'markers+text',
  marker = dict(symbol = 'marker', size = 15, color = 'blue'),
  text = hot_spot['Spot'], textposition = 'top center'))
  
fig.update_layout(title = dict(text = '에임스 주요시설', x = 0.5),
                  autosize = True, hovermode='closest',
                  mapbox = dict(accesstoken = 'pk.eyJ1IjoibmFtcSIsImEiOiJjbHpub2Q4bzUwc2ozMnBweXd4OW9mbm9mIn0.qc2xzGw9Za-ftKFZkDrCcA',
                                bearing = 0, center = dict(lon = -93.642897, lat = 42.034482),
                                pitch = 0, zoom = 12, style = 'light'))

fig.add_trace(go.Scattermapbox(
    lat=house['Latitude'],
    lon=house['Longitude'],
    mode='markers',
    marker=dict(symbol='circle', size=5, color='red'),
    text=house['Id'].astype(str),
    textposition='top right',
    hovertemplate='<b>House ID: %{text}</b><extra></extra>',
    name='Houses'))

fig.show()


# 나중에 혹시 카테고리별로 아이콘 바꿀때 사용할 코드======================================================================
hot_spot['Category'].unique()

spot_Cultural = hot_spot.query("Category == 'Cultural'")
spot_Education = hot_spot.query("Category == 'Education'")
spot_Leisure = hot_spot.query("Category == 'Leisure'")



fig = go.Figure(go.Scattermapbox(
  lat = spot_Cultural.iloc[:, -2], lon = spot_Cultural.iloc[:, -1],
  mode = 'markers+text',
  marker = dict(symbol = 'star', size = 15, color = 'blue'),
  text = hot_spot['Spot'], textposition = 'top center'))          # Cultureal 표시

fig.add_trace(go.Scattermapbox(
    lat=spot_Education.iloc[:, -2],
    lon=spot_Education.iloc[:, -1],
    mode='markers+text',
    marker=dict(symbol='star', size=15, color='blue'),
    text=hot_spot['Spot'],
    textposition='top center'))

fig.add_trace(go.Scattermapbox(
    lat=spot_Leisure.iloc[:, -2],
    lon=spot_Leisure.iloc[:, -1],
    mode='markers+text',
    marker=dict(symbol='star', size=15, color='blue'),
    text=hot_spot['Spot'],
    textposition='top center'))

fig.add_trace(go.Scattermapbox(
    lat=house['Latitude'],
    lon=house['Longitude'],
    mode='markers',
    marker=dict(symbol='circle', size=5, color='red'),
    text=house['Id'].astype(str),
    textposition='top right',
    hovertemplate='<b>House ID: %{text}</b><extra></extra>',
    name='Houses'))

fig.update_layout(title = dict(text = '에임스 주요시설', x = 0.5),
                  autosize = True, hovermode='closest',
                  mapbox = dict(accesstoken = 'pk.eyJ1IjoibmFtcSIsImEiOiJjbHpub2Q4bzUwc2ozMnBweXd4OW9mbm9mIn0.qc2xzGw9Za-ftKFZkDrCcA',
                                bearing = 0, center = dict(lon = -93.642897, lat = 42.034482),
                                pitch = 0, zoom = 12, style = 'light'))

fig.show()
#===========================================================================================================================








import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

house_train = pd.read_csv("./data/train.csv")
house_train.info()

house_train = house_train[['YrSold','MoSold', 'SalePrice']]

# 년도별로 group by 해서 Sale_Price의 평균 구하기
group_df = house_train.groupby(['YrSold', 'MoSold'])['SalePrice'].agg('mean').reset_index()

# --------------------------------
# 새로운 'YrMo' 컬럼을 생성하여 시간 축으로 사용
group_df['YrMo'] = group_df['MoSold'].astype(str) + '/' + group_df['YrSold'].astype(str)
group_df['YrMo'] = pd.to_datetime(group_df['YrMo'], format='%m/%Y')

# Plotly Express를 사용하여 선 그래프 생성
fig = px.line(group_df, 
              x='YrMo', 
              y='SalePrice', 
              title='월별 평균 SalePrice의 변화 (2006-2010)', 
              labels={'SalePrice':'Average SalePrice', 'YrMo':'Year-Month'})

# x축 레이블 회전 (가독성 향상)
fig.update_xaxes(tickangle=45)

# 그래프 표시
fig.show()
# --------------------------------






from scipy.stats import norm
norm.ppf(0.96, 60985, 10877)
train['SalePrice'].mean()






# 년도만 애니매이션
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# 데이터 로드 및 정보 확인
house_train = pd.read_csv("./data/train.csv")
house_train = house_train[['YrSold', 'MoSold', 'SalePrice']]

# 년도별로 group by 해서 Sale_Price의 평균 구하기
group_df = house_train.groupby(['YrSold', 'MoSold'])['SalePrice'].agg('mean').reset_index()

# 새로운 'YrMo' 컬럼을 생성하여 시간 축으로 사용
group_df['YrMo'] = group_df['MoSold'].astype(str) + '/' + group_df['YrSold'].astype(str)
group_df['YrMo'] = pd.to_datetime(group_df['YrMo'], format='%m/%Y')

# 애니메이션 프레임 생성 (연도별로 프레임 정의)
frames = []
years = sorted(group_df['YrMo'].dt.year.unique())

for year in years:
    filtered_df = group_df[group_df['YrMo'].dt.year == year]
    frames.append(go.Frame(
        data=[
            go.Scatter(
                x=filtered_df['YrMo'],
                y=filtered_df['SalePrice'],
                mode='markers+lines',
                marker=dict(color='red'),
                line=dict(color='blue', dash='dash'),
            )
        ],
        name=str(year)  # 연도를 프레임의 이름으로 사용
    ))

# 애니메이션을 처음 상태로 돌아가도록 하기 위한 빈 프레임 추가
frames.append(go.Frame(
    data=[
        go.Scatter(
            x=group_df['YrMo'],
            y=group_df['SalePrice'],
            mode='markers+lines',
            marker=dict(color='red'),
            line=dict(color='blue', dash='dash'),
        )
    ],
    name='Initial'  # 초기 상태로 돌아가는 프레임
))

# 레이아웃 정의
layout = go.Layout(
    title="2006-2010 월별 집가격 평균",
    xaxis=dict(title="Date", tickformat='%b %Y'),
    yaxis=dict(title="Mean Sale Price"),
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 2000, "redraw": True}, "fromcurrent": True, "mode": "immediate"}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ],
    sliders=[{
        "steps": [
            {
                "args": [
                    [str(year)],
                    {"frame": {"duration": 1000, "redraw": True}, "mode": "immediate", "transition": {"duration": 300}},
                ],
                "label": str(year),
                "method": "animate",
            }
            for year in years
        ] + [
            {
                "args": [[frames[-1].name], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                "label": 'Restart',
                "method": "animate",
            }
        ],
        "currentvalue": {"prefix": "Year: "},
        "transition": {"duration": 300, "easing": "cubic-in-out"},
    }],
)

# Figure 생성
fig = go.Figure(
    data=[
        go.Scatter(
            x=group_df['YrMo'],
            y=group_df['SalePrice'],
            mode='markers+lines',
            marker=dict(color='red'),
            line=dict(color='blue', dash='dash'),
        )
    ],
    layout=layout,
    frames=frames
)

# Figure 표시
fig.show()






# 일반
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# 데이터 로드 및 정보 확인
house_train = pd.read_csv("./data/train.csv")
house_train = house_train[['YrSold', 'MoSold', 'SalePrice']]

# 년도별로 group by 해서 Sale_Price의 평균 구하기
group_df = house_train.groupby(['YrSold', 'MoSold'])['SalePrice'].agg('mean').reset_index()

# 새로운 'YrMo' 컬럼을 생성하여 시간 축으로 사용
group_df['YrMo'] = group_df['MoSold'].astype(str) + '/' + group_df['YrSold'].astype(str)
group_df['YrMo'] = pd.to_datetime(group_df['YrMo'], format='%m/%Y')

# 애니메이션 프레임 생성 (월별로 프레임 정의)
frames = []
months = sorted(group_df['YrMo'].unique())

# 월별로 누적된 데이터를 포함하는 프레임 생성
for month in months:
    filtered_df = group_df[group_df['YrMo'] <= month]
    frames.append(go.Frame(
        data=[
            go.Scatter(
                x=filtered_df['YrMo'],
                y=filtered_df['SalePrice'],
                mode='markers+lines',
                marker=dict(color='red'),
                line=dict(color='blue', dash='dash'),
            )
        ],
        name=month.strftime('%b %Y')
    ))

# 고정된 프레임 (전체 데이터)
fixed_frame = go.Frame(
    data=[
        go.Scatter(
            x=group_df['YrMo'],
            y=group_df['SalePrice'],
            mode='markers+lines',
            marker=dict(color='red'),
            line=dict(color='blue', dash='dash'),
        )
    ],
    name='Fixed'
)

# 초기 상태로 돌아가는 프레임 추가
frames.append(fixed_frame)

# 구간별 레이블 생성
num_steps = 3
step_interval = len(months) // num_steps

# 슬라이더 스텝 생성
steps = [
    {
        "args": [
            [month.strftime('%b %Y')],
            {"frame": {"duration": 100, "redraw": True}, "mode": "immediate", "transition": {"duration": 300}},
        ],
        "label": month.strftime('%b %Y'),
        "method": "animate",
    }
    for i, month in enumerate(months)
] + [
    {
        "args": [[fixed_frame.name], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
        "label": 'Restart',
        "method": "animate",
    }
]

# 레이아웃 정의
layout = go.Layout(
    title="2006-2010년 월별 평균 집값",
    xaxis=dict(
        title="Date",
        tickformat='%b %Y',
        range=['2006-01-01', '2010-07-01']
    ),
    yaxis=dict(
        title="Mean Sale Price",
        range=[group_df['SalePrice'].min(), group_df['SalePrice'].max()]
    ),
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True, "mode": "immediate"}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ],
    sliders=[{
        "steps": steps,
        "currentvalue": {"prefix": "Date: "},
        "transition": {"duration": 300, "easing": "cubic-in-out"},
    }],
)

# Figure 생성
fig = go.Figure(
    data=[
        go.Scatter(
            x=group_df['YrMo'],
            y=group_df['SalePrice'],
            mode='markers+lines',
            marker=dict(color='red'),
            line=dict(color='blue', dash='dash'),
        )
    ],
    layout=layout,
    frames=frames
)

# Figure 표시
fig.show()









# 슬라이드 없고 범위설정
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# 데이터 로드 및 정보 확인
house_train = pd.read_csv("./data/train.csv")
house_train = house_train[['YrSold', 'MoSold', 'SalePrice']]

# 년도별로 group by 해서 Sale_Price의 평균 구하기
group_df = house_train.groupby(['YrSold', 'MoSold'])['SalePrice'].agg('mean').reset_index()

# 새로운 'YrMo' 컬럼을 생성하여 시간 축으로 사용
group_df['YrMo'] = group_df['MoSold'].astype(str) + '/' + group_df['YrSold'].astype(str)
group_df['YrMo'] = pd.to_datetime(group_df['YrMo'], format='%m/%Y')

# 애니메이션 프레임 생성 (월별로 프레임 정의)
frames = []
months = sorted(group_df['YrMo'].unique())

# 월별로 누적된 데이터를 포함하는 프레임 생성
for month in months:
    filtered_df = group_df[group_df['YrMo'] <= month]
    frames.append(go.Frame(
        data=[
            go.Scatter(
                x=filtered_df['YrMo'],
                y=filtered_df['SalePrice'],
                mode='markers+lines',
                marker=dict(color='red'),
                line=dict(color='blue', dash='dash'),
            )
        ],
        name=month.strftime('%b %Y')
    ))

# 고정된 프레임 (전체 데이터)
fixed_frame = go.Frame(
    data=[
        go.Scatter(
            x=group_df['YrMo'],
            y=group_df['SalePrice'],
            mode='markers+lines',
            marker=dict(color='red'),
            line=dict(color='blue', dash='dash'),
        )
    ],
    name='Fixed'
)

# 초기 상태로 돌아가는 프레임 추가
frames.append(fixed_frame)

# 레이아웃 정의
layout = go.Layout(
    title="2006-2010년 월별 평균 집값",
    xaxis=dict(
        title="Date",
        tickformat='%b %Y',
        range=['2005-12-01', '2010-08-01']
    ),
    yaxis=dict(
        title="Mean Sale Price",
        range=[group_df['SalePrice'].min()-5000, group_df['SalePrice'].max()+5000]
    ),
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True, "mode": "immediate"}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ],
    sliders=[]  # 슬라이더를 빈 리스트로 설정하여 제거
)

# Figure 생성
fig = go.Figure(
    data=[
        go.Scatter(
            x=group_df['YrMo'],
            y=group_df['SalePrice'],
            mode='markers+lines',
            marker=dict(color='red'),
            line=dict(color='blue', dash='dash'),
        )
    ],
    layout=layout,
    frames=frames
)

# Figure 표시
fig.show()






# 월별 집값 차이
group_df2 = house_train.groupby(['MoSold'])['SalePrice'].agg('mean').reset_index()
group_df

x = group_df2['MoSold']
y = group_df2['SalePrice']

fig = go.Figure(
  data = {
    'type' : 'scatter', 'mode' : 'markers+lines',
    'x' : x, 'y' : y,
    'marker' : {'color' : 'red'},
    'line' : {'color' : 'black', 'dash' : 'solid'},
    'showlegend' : False
  },
  layout = {
    'title'  : {'text' : "월별 집값 차이",
                'font' : {'size' : 25},
                'x' : 0.5},
    'xaxis'  : {'title' : 'month'},
    'yaxis'  : {'title' : 'SalePrice'},
    'margin' : {'t': 50, 'b' : 25, 'l' : 25, 'r' : 25}
  }
)

fig.show()






