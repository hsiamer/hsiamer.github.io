var form = new FormData(),  
    url = 'http://.......', //服务器上传地址  
    file = files[0];  
form.append('file', file);  
  
fetch(url, {  
    method: 'POST',  
    body: form  
}).then(function(response) {  
    if (response.status >= 200 && response.status < 300) {  
        return response;  
    }   
    else {  
        var error = new Error(response.statusText);  
        error.response = response;  
        throw error;  
    }  
}).then(function(resp) {  
    return resp.json();  
}).then(function(respData) {  
    console.log('文件上传成功', respData);  
}).catch(function(e) {  
    console.log('文件上传失败', e);  
});  