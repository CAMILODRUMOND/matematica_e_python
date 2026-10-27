import pandas as pd
import streamlit as st
import ploty as py

cores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

grupos = ['Branca', 'Preta ou Parda', 'Indígena']

for i, col in enumerate(grupos):
  axes[i].pie(
      df[col],
      labels=df['Meio de Transporte'],
      autopct='%1.2f%%', 
      colors=cores,
      wedgeprops={'edgecolor': 'white', 'linewidth': 1.2},
  )
  axes[i].set_title(f'Cor/Raça: {col}', fontsize=12, fontweight='bold')

plt.suptitle(
    'DE UM TÍTULO',
    fontsize=14,
    fontweight='bold',
)
plt.tight_layout()
plt.savefig('grafico_transporte.png', dpi=300)
plt.show()



st.set_page_config(page_title="Meu Dashboard ", layout="wide")

st.title("Dashboard ")

dates = pd.date_range(start="2022-01-01", periods=100, freq="D")
values = np.random.randn(100).cumsum()
df = pd.DataFrame({"Date": dates, "Value": values})


st.sidebar.header("Filtro")
cor_escolhida = st.sidebar.selectbox("Escolha a cor", ["blue", "green", "red", "purple"])


fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Date"], df["Value"], color=cor_escolhida, label="Série ")
ax.set_title("Gráfico de Exemplo")
ax.set_xlabel("Data")
ax.set_ylabel("Valor")
ax.legend()

st.pyplot(fig)

st.write("Streamlit loves LLMs! 🤖 [Build your own chat app](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) in minutes, then make it powerful by adding images, dataframes, or even input widgets to the chat.")

st.caption("Note that this demo app isn't actually connected to any LLMs. Those are expensive ;)")


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
           

        for chunk in assistant_response.split():
            full_response += chunk + " "

            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
