import React,{ useEffect } from 'react';
import { useDispatch,useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { fetchAllProducts } from '../../../store/product';
import { NavLink } from 'react-router-dom';
import "./Homepage.css";
import ImageSlider from './ImageSlider';


function Homepage() {

    const dispatch = useDispatch();
    const productsObj = useSelector(state => state.products)
    const allproducts=Object.values(productsObj)

    const history=useHistory();

    useEffect(() => {
        dispatch(fetchAllProducts());
    }, [dispatch]);


const slides =[
  {url:'https://m.media-amazon.com/images/I/61rKNNX+o+L._SX3000_.jpg',title:'Beach'},
  {url:'https://m.media-amazon.com/images/I/71DjHmMj+jL._SX3000_.jpg',title:'Boat'},
  {url:'https://m.media-amazon.com/images/I/71qKCoGx16L._SX3000_.jpg',title:'Flyer'},
  {url:'https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/c821b395-ef72-4351-911a-5c161e0ba640.jpg',title:'Go'},
  {url:'https://images-na.ssl-images-amazon.com/images/G/01/launchpad/2023/Events/NYNY/GW/DesktopTallHero_3000x1200_NYNY_LP_12.22._CB619040395_.jpg',title:'Bloom'},
]

const containerSytles = {
    width:'100vw',
    height:'700px',
    margin:"0 0",
};


    

    if(!productsObj) return null



    return (
        <div className='homepage-section'>
            <div className='homepage-firstsec'>
                <div style={containerSytles}>
                <ImageSlider slides={slides} allproducts={allproducts}/>
                </div>
            </div>

            <div className='homepage-secondsec'>
               <div className='sc-entire'>
               <div className='sc-first'>
               <img src={'https://media.tenor.com/UIJ9DZX6AR4AAAAd/atlantis.gif'} className="image"/>
               </div>
               <div className="sc-second">
               
               </div>
               <div className='sc-second'>

               </div>
               </div>
            </div>
            {/* <div className='homepage-list'>
            {allproducts.map(({ id, title,category,price,dicount,brand,imageUrl}) => (
            <div className='item' key={id}><NavLink to={`/products/${id}`}>
                <div className='itemimg'><img src={imageUrl} className="image"/></div>
                <div>{title}</div>
            </NavLink></div>
          ))}               
            </div> */}
        </div>
    )
}

export default Homepage;