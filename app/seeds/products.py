from app.models import db, Product, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_products():
    product1 = Product(
        creatorId=1,title='"Acer 27.0" 1920 x 1080 VA Zero-Frame Office Home Computer Monitor - AMD FreeSync - 75Hz Refresh - 1ms VRB - Low Blue Light Filter - Tilt and VESA Compatible - HDMI Port 1.4 & VGA Port KB272HL Hbi', category='Computers',price=159,discount=0.75,inventory=6,style='Modern',brand='Acer',color='black',dimension='9.8 x 24.2 x 17.4 inches',about='"27" full hd (1920 x 1080) widescreen va monitor with amd radeon freesync technology,Response time: 1ms vrb,Zero frame design,Refresh rate: 75hz,Ports: 1 x hdmi port & 1 x vga (vga cable included),Display technology: LED',description="Delve into the world of awesome with Acer's KB272HL Full HD monitor, which offers an unmatched viewing experience. A large 27” screen delivers astonishing, 1920 x 1080 Full HD resolution with excellent detail! Through AMD Radeon technology, the game’s frame rate is determined by your graphics card, not the fixed refresh rate of the monitor, giving you a serious competitive edge.",imageUrl='https://m.media-amazon.com/images/I/81fXRzLabWL._AC_SX679_.jpg')
    product2 = Product(
        creatorId=2, title='Dacoity Gaming Keyboard, 104 Keys All-Metal Panel, Rainbow LED Backlit Quiet Computer Keyboard, Wrist Rest, Multimedia Keys, Anti-ghosting Keys, Waterproof Light Up USB Wired Keyboard for PC Mac Xbox', category='Computers',price=29,discount=0.7,inventory=4,style='Modern',brand='Dacoity',color='grey',dimension='17.68 x 7.87 x 1.77 inches',about='This silent keyboard features a scientific stepped keycap design to maximize hand comfort for long hours of gaming or work. It also provides you with an ergonomic typing angle (7°) and wrist support during use. All keys have a soft feel and no loud clicks. It will not affect others when staying up late typing or playing games, it is very suitable for office or games.',description='Removable keycaps for quick cleaning without worrying about dust or dirt. Two-tone injection-molded keycaps provide crystal-clear uniform backlighting, and letters never fade.',imageUrl='https://m.media-amazon.com/images/I/715XLKbQnFL._AC_SX679_.jpg')
    product3 = Product(
        creatorId=3, title='Digital Camera for Photography VJIANGER 4K 48MP Vlogging Camera for YouTube with WiFi, 16X Digital Zoom, 52mm Wide Angle & Macro Lens, 2 Batteries, 32GB TF Card', category='Electronics',price=119,discount=0.95,inventory=20,style='Modern',brand='VJIANGER',color='black',dimension='7 x 3 x 5 inches',about='The 4k small digital camera with 30fps video resolution and 48 megapixel, provides a smooth shooting experience than 2.7K or 1080P video cameras, which can capture every excellent moment while vlog recording, the best camera for youtube. Equipped with wide angle & macro lenses and supports 16X Digital Zoom to get closer focus from far away and take close-up with clear details photos or recorder a wider range of scenery.',description="If you want a camera that can take good point-and-shoot images, and that comes at a value where if it's lost you won't have to deal with the same level of pain as losing a phone , this camera could very well be for you.This digital camera come with a new 48 Megapixel sensor make it have larger sensors than camera phones.Even cameras that use a comparatively smaller sensor have a good deal more surface area to work with than a smartphone sensor. This makes them not only can bring up great stills quality pictures ,but also much better for shooting in low light, as they can capture greater dynamic range of more detail in highlight and shadows.",imageUrl='https://m.media-amazon.com/images/I/81xi5JoLNmL._AC_SX679_.jpg')

    product4 = Product(
        creatorId=4, title='Countries of the World: Our World in Pictures Hardcover – November 24, 2020', category='Books',price=24,discount=0.78,inventory=20,style='Modern',brand='DK Children',color='White',dimension='5.25 x 0.25 x 11.25 inches',about='Did you know that Cuba’s national sport is baseball, one of the most popular sports in the US? And that kids in both Japan and Chile have earthquake drills on their school schedule? Find out about anything from the spookily vibrant Day of the Dead parade in Mexico and the beautiful springtime cherry blossom displays of Japan, to blueberry-picking in Sweden and India’s space program. Discover the countries of the world – explore their geography, wildlife, traditions, and arts, in this picture-packed children’s book.',description="This world encyclopedia includes at-a-glance panels that provide a quick reference to all the stats, making this engaging encyclopedia for kids an ideal combination of colorful diagrams and infographic text boxes with easy-to-read accessible text for readers aged 9-12, yet can be enjoyed by the entire family, making this enthralling children’s encyclopedia a beautiful and educational gift that can be passed down generations.",imageUrl='https://m.media-amazon.com/images/I/51sB-Lo5BYL._SX392_BO1,204,203,200_.jpg')

    product5 = Product(
        creatorId=4, title="Under Armour Men's Charged Assert 9 Running Shoe", category='Clothing,Shones',price=70,discount=0.78,inventory=40,style='Modern',brand='Under Armour',color='Black',dimension='15 x 5 x 9 inches',about='100% Textile,Made in the USA or Imported,Rubber sole,Heel measures approximately 1.4",Lightweight mesh upper with 3-color digital print delivers complete breathability,Durable leather overlays for stability & that locks in your midfoot, EVA sockliner provides soft, step-in comfort,Charged Cushioning midsole uses compression molded foam for ultimate responsiveness & durability,Solid rubber outsole covers high impact zones for greater durability with less weight',description="These running shoes are built to help anyone go faster-Charged Cushioning® helps protect against impact, leather overlays add durable stability, and a mesh upper keeps your feet cool for miles.. Lightweight mesh upper with 3-color digital print delivers complete breathability. Durable leather overlays for stability & that locks in your midfoot. EVA sockliner provides soft, step-in comfort. Charged Cushioning® midsole uses compression molded foam for ultimate responsiveness & durability. Solid rubber outsole covers high impact zones for greater durability with less weight. Offset: 10mm. NEUTRAL: For runners who need a balance of flexibility & cushioning. Lace type: Standard tie.",imageUrl='https://m.media-amazon.com/images/I/410-L0vF3+L._AC_UY695_.jpg')

    product6 = Product(
        creatorId=4, title="Nintendo Switch – OLED Model w/ White Joy-Con", category='Movies,Music&Games',price=348.5,discount=0.95,inventory=40,style='Classic',brand='Nintendo',color='Red',dimension='2.9 x 6.5 x 7.9 inches',about='7-inch OLED screen - Enjoy vivid colors and crisp contrast with a screen that makes colors pop, Wired LAN port - Use the dock’s LAN port when playing in TV mode for a wired internet connection,64 GB internal storage - Save games to your system with 64 GB of internal storage, Enhanced audio – Enjoy enhanced sound from the system’s onboard speakers when playing in Handheld and Tabletop modes.',description="Introducing the newest member of the Nintendo Switch family.Play at home on the TV or on-the-go with a vibrant 7-inch OLED screen with the Nintendo Switch – OLED Model system. In addition to a new screen with vivid colors and sharp contrast, the Nintendo Switch – OLED Model includes a wide adjustable stand for more comfortable viewing angles, a dock with a wired LAN port for TV mode (LAN cable sold separately), 64GB of internal storage, and enhanced audio in Handheld and Tabletop modes using the system’s speakers.",imageUrl='https://m.media-amazon.com/images/I/51yJ+OqktYL._SX466_.jpg')
    
    product7 = Product(
        creatorId=4, title="QCKJ Car Robot Toys,Deformation Robot Toy,Alloy Deformed Car Robot Toys, Optimus Action Figure with Weapon for Boy (Optimus Prime)", category='Toys,Kids&Baby',price=31.99,discount=0.94,inventory=40,style='Classic',brand='QCKJ',color='Red',dimension='8.6 x 3.9 x 7.4 inches',about='Car Transforming Toys,Converts between robot and truck models in 35 steps,comes with an extra head decoration.Similar to Optimus Prime Toy, Flexible joints, The toy package comes with a transformation instructions chart, you can easily convert the robot into a car.Car Action Figures Toys made of ABS plastic+Alloy material. Thick and durable, can handle the operation of children.Such as Optimus Prime, Collect the other 7-inch Commander series characters, so kids can imagine car robots battling the Decepticons.Robot Toys,Cool design and powerful 2 in 1 features, perfect gift for birthdays, Christmas, childrens day, parties and other festivals.',description="A Cassic Look, We have chosen the most embedded classic shapes for our collections because they bring out the true passion in every fan.",imageUrl='https://m.media-amazon.com/images/I/71HJVoFD9ZL._AC_SX466_.jpg')

    product8 = Product(
        creatorId=4, title="Massage Chair Zero Gravity Full Body Electric Shiatsu Massage Chair Recliner with Foot Rollers Built-in Heat Therapy Air Massage System Stretch Vibrating for Home Office(Black)", category='Beauty&Health',price=999,discount=0.6,inventory=30,style='Modern',brand='BestMassage',color='Black',dimension='56 x 30 x 45 inches',about='Our Massage Chair has a one-button for zero gravity angles for zero gravity massage chair, clicking the button to adjust a comfortable massage recliner chair reclining angle for massage chair zero gravity full body. Meanwhile, where is the point that our heart and knees are in a horizontal line, which can effectively not only reduce heart pressure but also stimulate blood circulation.Our Massage Chair is in a Easy way to use with remote controls, it will smoothly and safely control the lift without to left massage recliner chair,stay in your recline and massage of the chair. It helps you relax better in the massage chair. Our Massage Chair with lower back heat therapy is best ideal for strains of occasional strains and chronic pain.It offers the heat therapy which is a great compliment to the roller and airbag massage chair full body. Heating the body’s temperature is known to increase blood circulation and loosen tense muscles.',description="Feature The massage chair has zero-gravity function. There are total 32 air bags which are strategically located in the arms, hips, shoulder, thighs, calves, and feet, Multiple levels of intensity from strong to weak massage. Space saving technology only requires 10 inches from the wall. 2 heating pads in back area that enhance the massage experience. your muscles and joints will recover faster with increased blood circulation and less pain and aches. Our chairs are built to last and it is rated to accommodate a person who is 6'1 Tall and up to 350lbs, Easy to use control panel. 3 preset auto massage programs have different massage methods to give you the best massage experience. you can also choose power speed and airbag pressure to control your own massage. 100% tested before leaving the factory.",imageUrl='https://m.media-amazon.com/images/I/61UTXjYjeOL._AC_SX522_.jpg')

    

    


    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM products")
        
    db.session.commit()