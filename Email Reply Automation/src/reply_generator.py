import google.generativeai as genai
import os
from typing import Dict

class ReplyGenerator:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Email templates for different categories
        self.email_templates = {
            'Inquiry/Requests': """
            Dear [Customer's Name],
            Thank you for reaching out with your inquiry about [specific topic]. We appreciate your interest and are happy to assist.

            Based on your request, here is the information you need:
            1. [Key information 1]
            2. [Key information 2]
            3. [Key information 3]

            If you have any additional questions, feel free to reply to this email or contact us at [contact information]. We look forward to assisting you further.
            """,
            
            'Product Inquiry': """
            Dear [Customer's Name],
            Thank you for your inquiry about our [product name]. We are pleased to offer high-quality solutions tailored to your needs.

            Here are the details about [product name]:
            - Features: [Feature 1], [Feature 2], [Feature 3]
            - Price: [Pricing details]
            - Availability: [Stock or lead time information]

            Please let us know if you would like to place an order or need additional information. We are happy to assist.
            """,
            
            'Pricing Inquiry': """
            Dear [Customer's Name],
            Thank you for your interest in our [product/service name]. Here is the pricing information you requested:
            - Base Price: [Base price]
            - Discounts (if applicable): [Discount details]
            - Final Price: [Final price]

            If you need a detailed quote or further clarification, feel free to reply to this email or call us at [contact number]. We look forward to your response.
            """,
            
            'Technical Support': """
            Dear [Customer's Name],
            Thank you for contacting our technical support team regarding the issue with [product/service name]. We understand the inconvenience and are here to assist.

            Please follow these steps to resolve the issue:
            1. [Step 1]
            2. [Step 2]
            3. [Step 3]

            If the issue persists, please contact us again at [contact information]. We are committed to resolving this as quickly as possible.
            """,
            
            'General Inquiry': """
            Dear [Customer's Name],
            Thank you for reaching out to us. We value your inquiry and are happy to provide the information you need.

            Please provide additional details about your request so we can assist you more effectively. You can reach us directly at [contact information].

            We look forward to assisting you.
            """
        }
        
        self.company_details = """
        DEEPAK TECH INDIA specializes in manufacturing personalized water treatment plants:
        - STP (Sewage Treatment Plants)
        - ETP (Effluent Treatment Plants)
        - UF (Ultrafiltration)
        - RO (Reverse Osmosis) systems
        
        Contact: [Your contact details]
        Website: [Your website]
        Address: [Your address]
        """

    def _determine_inquiry_type(self, email_content: str) -> str:
        """Determine the type of inquiry based on email content."""
        keywords = {
            'price': 'Pricing Inquiry',
            'cost': 'Pricing Inquiry',
            'quote': 'Pricing Inquiry',
            'product': 'Product Inquiry',
            'specification': 'Product Inquiry',
            'technical': 'Technical Support',
            'problem': 'Technical Support',
            'issue': 'Technical Support',
        }
        
        email_lower = email_content.lower()
        for keyword, inquiry_type in keywords.items():
            if keyword in email_lower:
                return inquiry_type
        return 'General Inquiry'

    def _extract_product_name(self, email_content: str) -> str:
        """Extract mentioned product name from email content."""
        products = ['STP', 'ETP', 'UF', 'RO']
        email_upper = email_content.upper()
        for product in products:
            if product in email_upper:
                return product
        return "Not specified"

    def generate_reply(self, email_data: Dict) -> str:
        """Generates email reply using Gemini API with specialized prompt."""
        inquiry_type = self._determine_inquiry_type(email_data['body'])
        product_name = self._extract_product_name(email_data['body'])
        customer_name = email_data['sender'].split('<')[0].strip()

        prompt = f"""
        You are an intelligent and professional customer service assistant for DEEPAK TECH INDIA, a company that specializes in manufacturing personalized water treatment plants, including STP (Sewage Treatment Plants), ETP (Effluent Treatment Plants), UF (Ultrafiltration), and RO (Reverse Osmosis) systems. Your task is to craft polite, clear, and professional email responses to customer inquiries.

        Here is the customer's email:
        {email_data['body']}

        **Additional Context:**
        - Customer Name: {customer_name}
        - Inquiry Topic: {inquiry_type}
        - Specific Product Mentioned: {product_name}
        - Relevant Company Details: {self.company_details}

        **Email Template to Follow:**
        {self.email_templates[inquiry_type]}

        **Response Requirements:**
        1. Begin the email with a polite greeting, addressing the customer by name.
        2. Thank the customer for reaching out and acknowledge their inquiry.
        3. Provide accurate and helpful information related to their query or the mentioned product/service.
        4. Offer next steps, such as sharing additional resources, requesting further details, or encouraging them to contact you for assistance.
        5. Maintain a professional, courteous tone throughout the email.
        6. Include relevant technical specifications if the inquiry is about a specific product.
        7. If pricing is discussed, mention that detailed quotes are available upon request.
        8. Follow the structure of the provided email template while customizing the content to the specific inquiry.

        Write a professional email response that addresses their specific inquiry and demonstrates technical expertise.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating reply: {e}")
            return "" 