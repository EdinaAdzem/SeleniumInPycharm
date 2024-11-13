Task 1
https://masterschool.notion.site/Homework-XPath-6c4229bd4ea1461a941010bbeb35365f?pvs=97#ecc2554c147c4d47b20ed4be10a8af1a

# XPath Expressions - Task 1 - 1-15

```xpath
//h1[@id='mainTitle']  # 1. Main Heading (h1) Element
//a[text()='About Us']  # 2. "About Us" Navigation Link
//a[text()='Graphic Design']  # 3. "Graphic Design" Dropdown Link
//h4[text()='Jane Smith']  # 4. Team Member’s Name "Jane Smith"
//h3[text()='SEO Services']/following-sibling::p  # 5. Description for "SEO Services" (Paragraph Element)
//section[@id='services']//div[@class='service-item']  # 6. All Service Items in the "Our Services" Section
//input[@type='email' and @id='email']  # 7. Email Input Field in the Contact Form
//form[@id='contactForm']  # 8. Entire Contact Form
//footer/p  # 9. Footer Paragraph Element
(//div[@class='team']//h4)[1]  # 10. First Team Member's Name (h4)
//div[@class='service-item']/p)[2]  # 11. Description of the Second Service Item
//section[@id='contact']//h2  # 12. "Contact Us" Section Header (h2)
//a[text()='Services']/following-sibling::ul[@class='dropdown']//a  # 13. All Links in the "Services" Dropdown Menu
(//div[@class='team']//li)[1]  # 14. First List Item (li) Under "Our Team" Section
//form[@id='contactForm']//input[@type='submit' and @value='Send Message']  # 15. "Send Message" Button in the Contact Form
