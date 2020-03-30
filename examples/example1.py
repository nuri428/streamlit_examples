import streamlit as st


# for local cache
class LocalCache:
    def __init__(self):
        self.user_value = 0

    def init_value(self, value):
        self.user_value = 0

    def set_value(self, value):
        self.user_value = value

    def get_value(self):
        return self.user_value


# for cache 객체
# 이 함수는 LocalCache를 캐싱 처리 함
@st.cache(allow_output_mutation=True)
def get_instance():
    ins = LocalCache()
    return ins


def test_main1():
    min_val = 0
    max_val = 10
    gap = 1
    old_val = get_instance().get_value()

    st.write("screen 1")
    val = st.sidebar.slider("select value", min_val, max_val, value=old_val, step=gap)
    get_instance().set_value(val)
    st.write(f"you select {get_instance().get_value()}")


def test_main2():
    val = get_instance().get_value()
    st.write("screen 2")

    st.write(f"you select {val}")
    min_val = 0
    max_val = 10
    gap = 1

    val2 = st.sidebar.slider("select value", min_val, max_val, val, gap)
    get_instance().set_value(val2)
    st.write(f"you select {get_instance().get_value()}")


def main():
    choose_menu = st.selectbox("choose menu", (["menu1", "menu2"]))
    if choose_menu == "menu1":
        test_main1()
    elif choose_menu == "menu2":
        test_main2()


if __name__ == "__main__":
    main()
