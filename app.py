import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title("🎛️ نمایش گرافیکی المان‌های الکترونیکی")

# انتخاب نوع المان
element = st.selectbox(
    "المان مورد نظر را انتخاب کنید:",
    ["مقاومت (Resistor)", "سلف (Inductor)", "خازن (Capacitor)", "ترانزیستور (Transistor)"]
)

# امکان وارد کردن مقدار المان
if element == "مقاومت (Resistor)":
    value = st.text_input("مقدار مقاومت (مثلاً 10 kΩ):", "10 kΩ")
elif element == "سلف (Inductor)":
    value = st.text_input("مقدار سلف (مثلاً 1 mH):", "1 mH")
elif element == "خازن (Capacitor)":
    value = st.text_input("مقدار خازن (مثلاً 100 µF):", "100 µF")
else:  # ترانزیستور
    value = st.text_input("نوع ترانزیستور (مثلاً NPN یا PNP):", "NPN")

# رنگ سیم‌ها و بدنه
wire_color = st.color_picker("رنگ سیم‌ها", "#000000")
body_color = st.color_picker("رنگ بدنه المان", "#FFD700")

# ساخت نمودار
fig, ax = plt.subplots(figsize=(6, 2))

# رسم المان‌ها با مقدار
if element == "مقاومت (Resistor)":
    ax.plot([-2, -1], [0, 0], color=wire_color, linewidth=3)
    resistor = patches.Rectangle((-1, -0.4), 2, 0.8,
                                 linewidth=2, edgecolor=wire_color, facecolor=body_color)
    ax.add_patch(resistor)
    ax.plot([1, 2], [0, 0], color=wire_color, linewidth=3)
    ax.text(0, -0.6, value, ha='center', fontsize=12)
    ax.set_title("مقاومت (Resistor)", fontsize=14)

elif element == "سلف (Inductor)":
    ax.plot([-2, -1], [0, 0], color=wire_color, linewidth=3)
    for i in range(5):
        arc = patches.Arc((-1 + i * 0.4, 0), 0.4, 0.4, angle=0,
                           theta1=0, theta2=180, color=body_color, linewidth=3)
        ax.add_patch(arc)
    ax.plot([0.8, 2], [0, 0], color=wire_color, linewidth=3)
    ax.text(0, -0.6, value, ha='center', fontsize=12)
    ax.set_title("سلف (Inductor)", fontsize=14)

elif element == "خازن (Capacitor)":
    ax.plot([-2, -0.5], [0, 0], color=wire_color, linewidth=3)
    ax.plot([-0.5, -0.5], [-0.5, 0.5], color=body_color, linewidth=5)
    ax.plot([0.5, 0.5], [-0.5, 0.5], color=body_color, linewidth=5)
    ax.plot([0.5, 2], [0, 0], color=wire_color,linewidth=3)
    ax.text(0, -0.6, value, ha='center', fontsize=12)
    ax.set_title("خازن (Capacitor)", fontsize=14)

else:  # ترانزیستور
    ax.plot([-2, -1], [0, 0], color=wire_color, linewidth=3)  # پایه
    ax.plot([-1, 0], [0, 0], color=wire_color, linewidth=3)
    ax.plot([0, 0.7], [0, 1], color=wire_color, linewidth=3)  # کلکتور
    ax.plot([0, 0.7], [0, -1], color=wire_color, linewidth=3) # امیتر
    ax.arrow(0.4, -0.6, 0.1, -0.2, head_width=0.1, head_length=0.1, color='red')
    ax.text(-0.3, 0.1, "B", fontsize=12)
    ax.text(0.7, 1, "C", fontsize=12)
    ax.text(0.7, -1, "E", fontsize=12)
    ax.text(0, -1.2, value, ha='center', fontsize=12)
    ax.set_title(f"ترانزیستور ({value})", fontsize=14)

# تنظیمات ظاهری
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.axis("off")

# نمایش در Streamlit
st.pyplot(fig)