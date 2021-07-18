<template>
	<view class="advertisement" style="width: 100%;">
		<web-view :src="url" @message="message"></web-view>
	</view>
</template>
<script>
	export default {

		data() {
			return {
				url: "/static/post.html"
			}
		},
		onLoad(options) {
			var data = JSON.parse(options.token);
			var departmentName = JSON.parse(options.departmentName);
			this.url += "?token=" + encodeURIComponent(data) + "&departmentName=" + encodeURIComponent(departmentName);
		},
		 onBackPress(){
			uni.setStorageSync('current',1);
			
			console.log('111111111111111111111111111');
			
		},
		mounted() {},
		methods: {
			message(event) {
				console.log(event.detail.data);
			}
		}
	}
</script>
