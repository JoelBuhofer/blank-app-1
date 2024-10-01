import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Planzer & Friends",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Function to load images
def load_image(image_path):
    return Image.open(image_path)

# Import necessary libraries
from PIL import Image

# =========================
# Header Section
# =========================
def header():
    st.markdown(
        """
        <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        .header img {
            height: 60px;
        }
        .nav-links a {
            margin: 0 15px;
            color: #333;
            text-decoration: none;
            font-weight: bold;
        }
        .nav-links a:hover {
            color: #004080;
        }
        .nav-links .btn {
            background-color: #004080;
            color: #fff;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
        }
        .nav-links .btn:hover {
            background-color: #003060;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="header">
            <a href="#home"><img src="https://via.placeholder.com/150x60.png?text=Logo" alt="Planzer & Friends Logo"></a>
            <div class="nav-links">
                <a href="#home">Home</a>
                <a href="#benefits">Benefits</a>
                <a href="#features">Features</a>
                <a href="#faq">FAQ</a>
                <a href="#contact" class="btn">Contact Us</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Hero Section
# =========================
def hero_section():
    st.markdown(
        """
        <style>
        .hero {
            background-image: url('https://images.unsplash.com/photo-1521791136064-7986c2920216');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 100px 20px;
            position: relative;
        }
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
        }
        .hero-content {
            position: relative;
            max-width: 800px;
        }
        .hero-content h2 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        .hero-content p {
            font-size: 20px;
            margin-bottom: 30px;
            line-height: 1.5;
        }
        .hero-content .cta-button {
            background-color: #ff6600;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
        }
        .hero-content .cta-button:hover {
            background-color: #e65c00;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="home" class="hero">
            <div class="hero-content">
                <h2>Direct Access to Engaged Audiences</h2>
                <p>Increase your sales potential by being featured in notification emails from compatible brands. Tap into active and interested audiences, amplify your brand exposure, and achieve greater business growth.</p>
                <a href="#demo" class="cta-button">See Our Solutions in Action</a>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Demo Video Section
# =========================
def demo_video_section():
    st.markdown(
        """
        <style>
        .demo-video {
            padding: 60px 20px;
            text-align: center;
        }
        .demo-video h2 {
            color: #004080;
            margin-bottom: 20px;
        }
        .demo-video p {
            max-width: 600px;
            margin: 0 auto 40px;
            line-height: 1.5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section id="demo" class="demo-video">
            <h2>How It Works</h2>
            <p>See how your ads will appear in customers' inboxes and how they will be displayed to the end-customer.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    
    # Embed YouTube video
    st.video("https://www.youtube.com/watch?v=your_video_id")  # Replace with your video URL

# =========================
# Benefits Section
# =========================
def benefits_section():
    st.markdown(
        """
        <style>
        .benefits {
            padding: 60px 20px;
            background-color: #f9f9f9;
        }
        .benefit-item {
            display: flex;
            align-items: center;
            margin-bottom: 60px;
        }
        .benefit-item.reverse {
            flex-direction: row-reverse;
        }
        .benefit-content {
            flex: 1;
            padding: 20px;
        }
        .benefit-content h3 {
            color: #004080;
            margin-bottom: 15px;
        }
        .benefit-content p {
            margin-bottom: 20px;
            line-height: 1.5;
        }
        .benefit-content .cta-button {
            background-color: #004080;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
        }
        .benefit-content .cta-button:hover {
            background-color: #003060;
        }
        .benefit-image img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        @media (max-width: 768px) {
            .benefit-item {
                flex-direction: column;
            }
            .benefit-item.reverse {
                flex-direction: column;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="benefits" class="benefits">
            <h2 style="text-align: center; color: #004080;">Benefits</h2>
            
            <div class="benefit-item">
                <div class="benefit-content">
                    <h3>Increased Impressions Without Big Advertising Costs</h3>
                    <p>Get increased visibility in delivery tracking emails without investing in costly advertising campaigns.</p>
                    <a href="#contact" class="cta-button">Learn More</a>
                </div>
                <div class="benefit-image">
                    <img src="https://via.placeholder.com/400x300.png?text=Increased+Impressions" alt="Increased Impressions">
                </div>
            </div>
            
            <div class="benefit-item reverse">
                <div class="benefit-content">
                    <h3>Strategic Brand Partnerships</h3>
                    <p>Benefit from a network of brand partners to offer and receive cross-referrals, maximizing cross-selling between complementary companies.</p>
                    <a href="#contact" class="cta-button">Learn More</a>
                </div>
                <div class="benefit-image">
                    <img src="https://via.placeholder.com/400x300.png?text=Brand+Partnerships" alt="Brand Partnerships">
                </div>
            </div>
            
            <div class="benefit-item">
                <div class="benefit-content">
                    <h3>Our Data at Your Service</h3>
                    <p>Take advantage of all the delivery and consumption information we've been gathering for years, and which we'll share with you so that you can develop your business in the best place at the best time.</p>
                    <a href="#contact" class="cta-button">Learn More</a>
                </div>
                <div class="benefit-image">
                    <img src="https://via.placeholder.com/400x300.png?text=Data+Service" alt="Data Service">
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Features Section
# =========================
def features_section():
    st.markdown(
        """
        <style>
        .features {
            padding: 60px 20px;
        }
        .features h2 {
            text-align: center;
            color: #004080;
            margin-bottom: 40px;
        }
        .features-list {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }
        .feature-item {
            background-color: white;
            border: 1px solid #ddd;
            flex: 1 1 calc(33.333% - 40px);
            padding: 30px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .feature-item i {
            font-size: 48px;
            color: #004080;
            margin-bottom: 20px;
        }
        .feature-item h4 {
            margin-bottom: 15px;
            color: #004080;
        }
        .feature-item p {
            color: #666;
            line-height: 1.5;
        }
        @media (max-width: 768px) {
            .feature-item {
                flex: 1 1 100%;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="features" class="features">
            <h2>Features</h2>
            <div class="features-list">
                <div class="feature-item">
                    <i class="fas fa-chart-line"></i>
                    <h4>Real-Time Analytics</h4>
                    <p>Get instant insights into your campaign performance.</p>
                </div>
                <div class="feature-item">
                    <i class="fas fa-user-friends"></i>
                    <h4>Customer Engagement</h4>
                    <p>Interact with a highly engaged audience.</p>
                </div>
                <div class="feature-item">
                    <i class="fas fa-shield-alt"></i>
                    <h4>Data Security</h4>
                    <p>Your data is protected with top-tier security measures.</p>
                </div>
                <!-- Add more feature items as needed -->
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Community CTA Section
# =========================
def community_section():
    st.markdown(
        """
        <style>
        .community {
            padding: 60px 20px;
            text-align: center;
            background-color: #f9f9f9;
        }
        .community h2 {
            color: #004080;
            margin-bottom: 20px;
        }
        .community p {
            max-width: 600px;
            margin: 0 auto 30px;
            line-height: 1.5;
        }
        .community .cta-button {
            background-color: #ff6600;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
        }
        .community .cta-button:hover {
            background-color: #e65c00;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="community" class="community">
            <h2>Join Our Private Community</h2>
            <p>Get access to our private community giving you the latest important information on e-commerce trends in Switzerland.</p>
            <a href="#contact" class="cta-button">Join Now</a>
        </section>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Objections and Reassurances Section
# =========================
def objections_section():
    st.markdown(
        """
        <style>
        .objections {
            padding: 60px 20px;
        }
        .objections h2 {
            text-align: center;
            color: #004080;
            margin-bottom: 40px;
        }
        .accordion-item {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
            padding: 15px;
        }
        .accordion-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
        }
        .accordion-header h3 {
            margin: 0;
            font-size: 18px;
            color: #004080;
        }
        .accordion-header i {
            transition: transform 0.3s ease;
        }
        .accordion-item.open .accordion-header i {
            transform: rotate(180deg);
        }
        .accordion-content {
            margin-top: 10px;
            display: none;
        }
        .accordion-item.open .accordion-content {
            display: block;
        }
        .accordion-content p {
            margin: 0;
            color: #666;
            line-height: 1.5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="objections" class="objections">
            <h2>Your Concerns Addressed</h2>
            <div class="accordion">
                <div class="accordion-item">
                    <div class="accordion-header">
                        <h3>Data Protection Compliance</h3>
                        <i class="fas fa-chevron-down"></i>
                    </div>
                    <div class="accordion-content">
                        <p>We are in compliance with EU data protection laws.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <div class="accordion-header">
                        <h3>Legal Foundations</h3>
                        <i class="fas fa-chevron-down"></i>
                    </div>
                    <div class="accordion-content">
                        <p>The legal foundations for our personalized ads are within our terms and conditions, which the customer will accept when they click on the "Sendung verfolgen" button in the tracking email.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <div class="accordion-header">
                        <h3>High Conversion Rates</h3>
                        <i class="fas fa-chevron-down"></i>
                    </div>
                    <div class="accordion-content">
                        <p>We get an average of 10 conversions per 100 leads, which is above industry standard.</p>
                    </div>
                </div>
                <div class="accordion-item">
                    <div class="accordion-header">
                        <h3>Exclusive Offer</h3>
                        <i class="fas fa-chevron-down"></i>
                    </div>
                    <div class="accordion-content">
                        <p>The first few customers get Planzer & Friends free for the first 5 years.</p>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    
    # Add JavaScript for accordion functionality
    st.markdown(
        """
        <script>
        const accordionItems = document.querySelectorAll('.accordion-item');
        
        accordionItems.forEach(item => {
            const header = item.querySelector('.accordion-header');
        
            header.addEventListener('click', () => {
                const openItem = document.querySelector('.accordion-item.open');
        
                toggleItem(item);
        
                if (openItem && openItem !== item) {
                    toggleItem(openItem);
                }
            });
        });
        
        function toggleItem(item) {
            const content = item.querySelector('.accordion-content');
            const icon = item.querySelector('.accordion-header i');
        
            if (item.classList.contains('open')) {
                content.style.display = 'none';
                item.classList.remove('open');
            } else {
                content.style.display = 'block';
                item.classList.add('open');
            }
        }
        </script>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Social Proof Section
# =========================
def social_proof_section():
    st.markdown(
        """
        <style>
        .social-proof {
            padding: 60px 20px;
            background-color: #f9f9f9;
            text-align: center;
        }
        .social-proof h2 {
            color: #004080;
            margin-bottom: 40px;
        }
        .social-proof .logos {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 40px;
        }
        .social-proof .logos img {
            max-width: 150px;
            filter: grayscale(100%);
            transition: filter 0.3s ease;
        }
        .social-proof .logos img:hover {
            filter: grayscale(0%);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="social-proof" class="social-proof">
            <h2>Trusted by Leading Companies</h2>
            <div class="logos">
                <img src="https://via.placeholder.com/150x80.png?text=Company+1" alt="Company 1">
                <img src="https://via.placeholder.com/150x80.png?text=Company+2" alt="Company 2">
                <img src="https://via.placeholder.com/150x80.png?text=Company+3" alt="Company 3">
                <!-- Add more logos as needed -->
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

# =========================
# FAQ Section
# =========================
def faq_section():
    st.markdown(
        """
        <style>
        .faq {
            padding: 60px 20px;
        }
        .faq h2 {
            text-align: center;
            color: #004080;
            margin-bottom: 40px;
        }
        .faq-item {
            max-width: 800px;
            margin: 0 auto 30px;
        }
        .faq-item h3 {
            color: #004080;
            margin-bottom: 10px;
        }
        .faq-item p {
            color: #666;
            line-height: 1.5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="faq" class="faq">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-item">
                <h3>How does Planzer & Friends handle data privacy?</h3>
                <p>We strictly adhere to EU data protection laws to ensure your data is safe and secure.</p>
            </div>
            <div class="faq-item">
                <h3>What is the cost after the first 5 years?</h3>
                <p>We offer competitive pricing models tailored to your business needs. Contact us for detailed information.</p>
            </div>
            <!-- Add more FAQ items as needed -->
        </section>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Contact Section
# =========================
def contact_section():
    st.markdown(
        """
        <style>
        .contact {
            padding: 60px 20px;
            background-color: #004080;
            color: white;
            text-align: center;
        }
        .contact h2 {
            margin-bottom: 20px;
        }
        .contact p {
            max-width: 600px;
            margin: 0 auto 30px;
            line-height: 1.5;
        }
        .contact form {
            max-width: 600px;
            margin: 0 auto;
        }
        .contact input, .contact textarea {
            width: 100%;
            padding: 15px;
            margin-bottom: 15px;
            border: none;
            border-radius: 5px;
        }
        .contact button {
            background-color: #ff6600;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .contact button:hover {
            background-color: #e65c00;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <section id="contact" class="contact">
            <h2>Get in Touch</h2>
            <p>Ready to take your business to the next level? Contact us today!</p>
        </section>
        """,
        unsafe_allow_html=True,
    )
    
    # Streamlit form
    with st.form(key='contact_form', clear_on_submit=True):
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email")
        message = st.text_area("Your Message", placeholder="Enter your message")
        submit_button = st.form_submit_button(label='Send Message')
    
    if submit_button:
        # Here you can add code to handle form submission, e.g., send an email or store in a database
        st.success("Thank you for reaching out! We'll get back to you shortly.")

# =========================
# Footer Section
# =========================
def footer():
    st.markdown(
        """
        <style>
        .footer {
            background-color: #f2f2f2;
            padding: 20px;
            text-align: center;
        }
        .footer p {
            margin: 0;
            color: #333;
        }
        .footer nav ul {
            list-style-type: none;
            padding: 0;
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 10px;
        }
        .footer nav ul li a {
            color: #004080;
            text-decoration: none;
        }
        .footer nav ul li a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <footer class="footer">
            <p>&copy; 2023 Planzer & Friends. All rights reserved.</p>
            <nav>
                <ul>
                    <li><a href="#privacy">Privacy Policy</a></li>
                    <li><a href="#terms">Terms and Conditions</a></li>
                </ul>
            </nav>
        </footer>
        """,
        unsafe_allow_html=True,
    )

# =========================
# Main Function to Render Sections
# =========================
def main():
    header()
    hero_section()
    demo_video_section()
    benefits_section()
    features_section()
    community_section()
    objections_section()
    social_proof_section()
    faq_section()
    contact_section()
    footer()

if __name__ == "__main__":
    main()
