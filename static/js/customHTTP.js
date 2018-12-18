class EasyHTTP {
   
  getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}  
    // Make an HTTP GET Request 

    get(url) {
      return new Promise((resolve, reject) => {
        fetch(url)
        .then(res => res.json())
        .then(data => resolve(data))
        .catch(err => reject(err));
      });
    }
  
    // Make an HTTP POST Request
    
    post(url, data) {
      var name = "csrftoken"
      return new Promise((resolve, reject) => {
        fetch(url, {
          method: 'POST',
          headers: {
            "X-CSRFToken": Cookies.get('csrftoken'),
            "Accept": "application/json",
            "Content-type": "application/json"
          },
          body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => resolve(data))
        .catch(err => reject(err));
      });
    }
  
     // Make an HTTP PUT Request
     put(url, data) {
      return new Promise((resolve, reject) => {
        fetch(url, {
          method: 'PUT',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => resolve(data))
        .catch(err => reject(err));
      });
    }
  
    // Make an HTTP DELETE Request
    delete(url) {
      return new Promise((resolve, reject) => {
        fetch(url, {
          method: 'DELETE',
          headers: {
            'Content-type': 'application/json'
          }
        })
        .then(res => res.json())
        .then(() => resolve('Resource Deleted...'))
        .catch(err => reject(err));
      });
    }
  
   }
  