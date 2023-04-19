import streamlit as st

def find_greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def main():

    st.title('Find the greatest among three numbers')
    st.write('Enter three numbers below:')
    a = st.number_input('Enter the first number:')
    b = st.number_input('Enter the second number:')
    c = st.number_input('Enter the third number:')
    
    if st.button('Find the greatest'):

        answer = find_greatest(a, b, c)
        st.success("The largest number is" + answer)


if __name__ == "__main__":
    main()
