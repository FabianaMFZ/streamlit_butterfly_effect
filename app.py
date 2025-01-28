import streamlit as st
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

# Function to generate Lorentz Attractor data
def lorentz_attractor(sigma=10., beta=8./3, rho=28.0, N=10000, dt=0.01):
    # Initialize arrays for x, y, z positions
    x, y, z = np.empty(N), np.empty(N), np.empty(N)
    x[0], y[0], z[0] = np.random.uniform(-15, 15), np.random.uniform(-15, 15), np.random.uniform(5, 55)
    
    for i in range(1, N):
        dx = sigma * (y[i-1] - x[i-1])
        dy = x[i-1] * (rho - z[i-1]) - y[i-1]
        dz = x[i-1] * y[i-1] - beta * z[i-1]
        
        # Update positions
        x[i] = x[i-1] + dx * dt
        y[i] = y[i-1] + dy * dt
        z[i] = z[i-1] + dz * dt
        
    return x, y, z

# Generate Lorentz Attractor data
N = 10000
x, y, z = lorentz_attractor(N=N)

# Create the Plotly animation
def lorentz_attractor_animation(x, y, z):
    plotly_template = pio.templates["plotly_dark"]
    
    # Create the 3D scatter plot with frames for animation
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines',
                                       line=dict(width=1.8,
                                                 color=z,
                                                 colorscale='Plotly3',
                                                 showscale=False
                                       ))], frames=[
        go.Frame(data=[go.Scatter3d(x=x[:k], y=y[:k], z=z[:k], mode='lines')])
        for k in range(1, len(x), 50)
    ])
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(backgroundcolor='rgb(20, 20, 20)', showgrid=False, zerolinecolor='rgb(50, 50, 50)'),
            yaxis=dict(backgroundcolor='rgb(20, 20, 20)', showgrid=False, zerolinecolor='rgb(50, 50, 50)'),
            zaxis=dict(backgroundcolor='rgb(20, 20, 20)', showgrid=False, zerolinecolor='rgb(50, 50, 50)')
        ),
        paper_bgcolor='rgb(20, 20, 20)',
        font=dict(color='black'),
        updatemenus=[dict(type='buttons', showactive=False,
                          buttons=[dict(label='Play', method='animate', args=[None, {'frame': {'duration': 2, 'redraw': True},
                                                                                 'fromcurrent': True, 'mode': 'immediate'}])],
                          direction='left',
                          pad=dict(r=10, t=87),
                          x=0.1,
                          xanchor='right',
                          y=0,
                          yanchor='top',
                          bgcolor='white',
                          bordercolor='white',
                          font=dict(color='white')
                          )
        ],
    )
    return fig

# Streamlit app interface
def main():
    st.title("Lorentz Attractor Animation")

    # Display the interactive Plotly animation
    st.plotly_chart(lorentz_attractor_animation(x, y, z))

if __name__ == "__main__":
    main()
