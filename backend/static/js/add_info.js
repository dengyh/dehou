function add_info(url) {
	// 上传封面图片事件
    $('#uploadBtn').click(function(){
        $("input[name='img']").trigger("click");
    });

    // 文本框内容不为空
    $('.alt_btn').click(function(){
        var ue = UE.getEditor('id_content');
        ue.ready(function() {
            if (ue.getContent().length <= 0) {
                alert("内容不能为空！");
                return false;
            }
            if ($("input[name='title']").val().length > 150 ||
                $("input[name='remark']").val().length > 150) {
                alert("标题或产品描述文字不能超过150个字");
                return false;
            }
            form.action = url;
        });
    });

    // 文本置空
    $('.clear_btn').click(function() {
        var ue = UE.getEditor('id_content');
        ue.ready(function() {
            if (confirm("确定要清空文本内容吗？")) {
                ue.setContent('');
            }
        });
    });
}