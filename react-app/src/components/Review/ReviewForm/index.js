import { useState,useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchCreateReview,fetchUpdateReview } from '../../../store/review';
import "./ReviewForm.css"

const ReviewForm=({theReview,formType,theProduct})=>{

    let initComments,initStars;
    const history=useHistory()
    const dispatch = useDispatch();
    
    if(formType==="Edit Review"){
        initComments=theReview.comments;
        initStars=theReview.stars;
    }
    else{
        initComments='';
        initStars=0;
    }

    const [comments, setComments] = useState(initComments);
    const [stars, setStars] = useState(initStars);
    
    const [validationErrors, setValidationErrors] = useState([]);

    useEffect(() => {
        if (!comments&&!stars) {
          setValidationErrors([]);
          return;
        }
        const errors =[];
        if(comments.length<=0){errors.push("Listing's review field is required");}
        if(isNaN(stars)){errors.push("Listing's stars must be a number");}

        setValidationErrors(errors);
  
      }, [comments,stars]);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (validationErrors.length) return;

        const tempReview = { ...theReview, comments,stars };
        const errors =[];

        if(formType==="Create Review"){
          dispatch(fetchCreateReview(tempReview,theProduct.id))
          .then(()=>history.push(`/orderdetails`))
          .catch(async (err)=>{
              const errobj=await err.json();
              errors.push(errobj.message)
              setValidationErrors(errors)
          });
          }
        else if(formType==="Edit Review"){
          dispatch(fetchUpdateReview(tempReview))
          .then(()=>history.push(`/orderdetails`))
          .catch(async (err)=>{
             const  errobject=await err.json();
            errors.push(errobject.message)
            setValidationErrors(errors)
          });
        }
      };      


    return(
        <div className='reviewform-section'>
        <h3 className="reviewform-title">{formType}</h3>
        
        {(!!theProduct) &&(
        <div className='rf-titlesection'>
        <div>
            <img  src={theProduct.imageUrl} className="productlist-image"
                          onError={e => { e.currentTarget.src = "https://www.shutterstock.com/image-vector/coming-soon-under-construction-yellow-600w-1746344219.jpg"; }}
                        />
        </div>
        <div>
            <div>{theProduct.title}</div>
        </div>
        
        </div>
        )}
        
        <form className='reviewform-form' onSubmit={handleSubmit}>

        {!!validationErrors.length && 
        <div className="reviewform-errorload">
        <div className="reviewform-erroricon"><i className="fa-solid fa-circle-exclamation" /></div>
        <div className="reviewform-errorinfo">
        <div className="reviewform-errortile">Input validation</div>
        <div>
          {validationErrors.map((error, idx) => (
            <div key={idx} className="reviewform-errortext">{error}</div>
          ))}
        </div>
        </div>
        </div>
        }
          <div className="reviewform-infomation">
          
          <div className='rf-ratesec'>
          <div className='rf-ratetitle'>Overall rating</div>
          <div className="rate">
          <input type="radio" id="star5" name="rate" value="5" 
          onChange={(e) => setStars(e.target.value)}
          checked={stars == "5"}
          />
          <label htmlFor="star5" >5 stars</label>
          <input type="radio" id="star4" name="rate" value="4" 
          onChange={(e) => setStars(e.target.value)}
          checked={stars == "4"}
          />
          <label htmlFor="star4" >4 stars</label>
          <input type="radio" id="star3" name="rate" value="3" 
          onChange={(e) => setStars(e.target.value)}
          checked={stars == "3"}
          />
          <label htmlFor="star3" >3 stars</label>
          <input type="radio" id="star2" name="rate" value="2" 
          onChange={(e) => setStars(e.target.value)}
          checked={stars == "2"}
          />
          <label htmlFor="star2" >2 stars</label>
          <input type="radio" id="star1" name="rate" value="1" 
           onChange={(e) => setStars(e.target.value)}
           checked={stars == "1"}         
          />
          <label htmlFor="star1" >1 star</label>
          </div>
         </div>
          

         <div className="rf-review">
          <label className="rf-text">
          Add a written review</label>
          <textarea
          placeholder='What did you like or dislike? What did you use this product for?'
          type="text"
          name="comments"
          onChange={(e) => setComments(e.target.value)}
          value={comments}/></div>

         </div>

         <input type="submit" value={`Submit`} className='rf-button'/>
        </form>
        </div>
     )

}

export default ReviewForm;   