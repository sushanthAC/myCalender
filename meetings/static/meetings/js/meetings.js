// function deleteMeeting(meeting) {
// 	var meeting = $(meeting)
// 	meeting.parent().remove()
// 	var meeting_id = meeting.data('id')
	
// 	$.ajax({
// 		url: 'meetings/delete/' + meeting_id,
// 		method: 'DELETE',
// 		beforeSend: function(xhr){
// 			xhr.setRequestHeader('X-CSRFToken', csrf_token)
// 		}
// 	})
// }