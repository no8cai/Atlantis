import { useState } from "react"
import { NavLink } from "react-router-dom";
import "./Homepage.css";


const ImageSlider=({slides,allproducts})=>{

    const [currentIndex, setCurrentIndex]=useState(0)

    let topdeal=allproducts[0]
    
    allproducts.forEach(el=>{
       if(el.discount<topdeal.discount){
            topdeal=el
       }
    })
    console.log(topdeal)

    const sliderStyles = {
        height:'100%',
        position:'relative',
    }

    const slidesStyles={
        width:'100%',
        height:'100%',
        backgroundPosition:'center',
        backgroundSize:'cover',
        backgroundImage:`url(${slides[currentIndex].url})`,
        transition:'ease-in-out 0.5s',
    }

    const leftArrowStyles={
        position:'absolute',
        top:'30%',
        transform:'translate(0,-50%)',
        left:'32px',
        fontSize:'45px',
        color:'#fff',
        zIndex:1,
        cursor:'pointer',
    }

    const rightArrowStyles={
        position:'absolute',
        top:'30%',
        transform:'translate(0,-50%)',
        right:'32px',
        fontSize:'45px',
        color:'#fff',
        zIndex:1,
        cursor:'pointer',
    }
    const goToPrevious=()=>{
        const isFristSlide=currentIndex===0
        const newIndex=isFristSlide?slides.length-1:currentIndex-1;
        setCurrentIndex(newIndex)
    }

    const goToNext=()=>{
        const isLastSlide=currentIndex===slides.length-1;
        const newIndex=isLastSlide?0:currentIndex+1
        setCurrentIndex(newIndex)
    }

    const selectobject=(arr)=>{
        return arr[0-2]
    }



    return (
       <div style={sliderStyles}>
        <div style={leftArrowStyles} onClick={goToPrevious} className='imageslider-arrowleft'><i className="fa-solid fa-chevron-left"/></div>
        <div style={rightArrowStyles} onClick={goToNext} className='imageslider-arrowright'><i className="fa-solid fa-chevron-right"/></div>
        <div className="top-section">
        <div className="top-first">
            <div className="top-sectiontitle">Items you may like</div> 
            <div className='firstsec-left'>
            {allproducts.map(({ id, title,imageUrl}) => (
            <div className='is-item' key={id}><NavLink to={`/products/${id}`} className='is-link'>
                <div className='is-itemimg'><img src={imageUrl} className="image"/></div>
                <div>{title}</div>
            </NavLink></div>
            
          ))}
            </div>       
        </div>
        <div className="top-first">
            <div className="top-sectiontitle">Hot items</div>
            <div className='firstsec-left'>
           {allproducts.map(({ id, title,imageUrl}) => (
            <div className='is-item' key={id}><NavLink to={`/products/${id}`} className='is-link'>
                <div className='is-itemimg'><img src={imageUrl} className="image"/></div>
                <div>{title}</div>
            </NavLink></div>
            
            ))}
            </div>
        </div>
        <div className="top-first">
        <div className="top-sectiontitle">Best deal of the Day</div>
        <NavLink to={`/products/${topdeal?topdeal.id:1}`} className='is-link'>
        <div className="top-thirditem">
           <img src={topdeal?topdeal.imageUrl:"http:imge.png"}/>
        </div>
        
        <div className="top-discount">{topdeal?`Up to ${((1-topdeal.discount)*100).toFixed(2)}% off`:""}</div>
        <div>{topdeal?topdeal.title:""}</div>
        </NavLink>
        </div>

        <div className="top-first">
        <div className="top-sectiontitle">Reach your goal with us</div>
        </div>
        </div>
         <div style={slidesStyles}></div>
       </div>
    )
    
}
export default ImageSlider