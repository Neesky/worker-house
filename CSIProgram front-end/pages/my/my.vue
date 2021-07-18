<template>
	<view>

		<view class="box1">
			<image style=" height: 200px;width: 200px;margin: 0 auto;" :src="avatar" id="avatar"></image>
			<text style="margin: 0 auto;font-size: 22px;font-weight: 600;color: #4D386F;">{{texts.name}}</text>
			<text style="margin-top:4%;margin-left: 25%;font-size: 15px;color: #4D386F;"
				space="emsp">{{"工号: "+texts.id}}</text>
			<text style="margin-left: 25%;font-size: 15px;color: #4D386F;"
				space="emsp">{{"部门: "+texts.departmentName}}</text>
			<text style="margin-left: 25%;font-size: 15px;color: #4D386F;" space="emsp">{{"职位: "+texts.jobName}}</text>
		</view>

		<view class="box2" @click="click_my_information">
			<image style="padding-left:5%;width: 35px;height: 35px;" src="/static/my_information.png">
			</image>
			<text style="color: #553D78;font-size: 19px;padding-left: 10%;font-weight: 700;">我的信息</text>
			<image style="margin-left:30%;padding-top:1%;height:25px;width: 25px;" src="/static/right.png"></image>
		</view>

		<view class="box3" @click="click_change_passward">
			<image style="padding-left:5%;width: 35px;height: 35px;" src="/static/change_password.png">
			</image>
			<text style="color: #553D78;font-size: 19px;padding-left: 10%;font-weight: 700;">修改密码</text>
			<image style="margin-left:30%;padding-top:1%;height:25px;width: 25px;"
				src="/static/right.png"></image>
		</view>

		<view class="box4" @click="click_exit">
			<image style="padding-left:5%;width: 35px;height: 35px;" src="/static/cancellation.png">
			</image>
			<text style="color: #553D78;font-size: 19px;padding-left: 10%;font-weight: 700;">注销</text>
			<image style="margin-left:42%;paddind-left:80%;padding-top:1%;height:25px;width: 25px;"
				src="/static/right.png"></image>
		</view>

		<view>
			<u-toast ref="uToast" />
		</view>

		<u-modal v-model="show_modal" :show-confirm-button="true" :show-cancel-button=true @confirm="confirm" content="注销操作将会解除账号与设备的绑定,确认注销？"
			:show-title="false"></u-modal>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				texts: {},
				avatar: "/static/avatar_boy.png",
				show_modal:false
			}
		},
		onShow() {
			uni.request({
				url: uni.getStorageSync('dd') + 'employee/myId',
				data: {
					"id": uni.getStorageSync('global_ID')
				},
				method: 'POST',
				header: {
					"token": uni.getStorageSync('token')
				},
				fail: (res) => {
					console.log(res.data);
				},
				success: (res) => {
					console.log(res.data);
					if (res.data.code == 200) {
						this.texts = res.data.data;
						if (this.texts.sex == "2") {
							this.avatar = "/static/avatar_girl.png";
						}
					} else {
						this.showToast(res.data.message);
					}
				}
			})
		},
		methods: {
			showToast(Msg) {
				this.$refs.uToast.show({
					title: Msg,
					type: 'error'
				})
			},
			click_my_information() {
				uni.navigateTo({
					url: './myInformation'
				})
			},
			click_change_passward() {
				uni.navigateTo({
					url: './changePassword'
				})
			},
			click_exit() {
				this.show_modal=true;
			},
			confirm(){
				uni.request({
					url: uni.getStorageSync('dd')+'login/logout',
					data: {
						"id": uni.getStorageSync('global_ID')
					},
					method: 'POST',
					header: {
						"token": uni.getStorageSync('token')
					},
					fail:(res)=>{
						console.log(res.data);
					},
					success: (res) => {
						if (res.data.code == 200) {
							uni.removeStorageSync('global_ID');
							uni.removeStorageSync('global_status');
							uni.removeStorageSync('global_password');
							uni.removeStorageSync('global_oaid');
							uni.removeStorageSync('global_employee_list');
							uni.removeStorageSync('global_department_list');
							uni.removeStorageSync('global_job_list');
							uni.removeStorageSync('current');
							uni.removeStorageSync('global_announcement_list');
							uni.removeStorageSync('global_read_list');
							uni.removeStorageSync('global_unread_list');
							uni.reLaunch({
								url:'../login/login'
							});
						} else {
							this.showToast(res.data.message);
						}
					}
				});
			}
		}
	}
</script>

<style>
	.box1 {
		padding-top: 4%;
		padding-bottom: 4%;
		margin-top: 4%;
		margin-left: 7%;
		margin-right: 7%;
		background-color: #F1EFFC;
		display: flex;
		flex-direction: column;
		border-radius: 40px;
	}

	.box2 {
		padding-top: 4%;
		padding-bottom: 4%;
		margin-top: 6%;
		margin-left: 7%;
		margin-right: 7%;
		background-color: #F0E9E9;
		display: flex;
		border-radius: 20px;
		height: 120rpx;

	}

	.box3 {
		padding-top: 4%;
		padding-bottom: 4%;
		margin-top: 6%;
		margin-left: 7%;
		margin-right: 7%;
		background-color: #F0FAE9;
		display: flex;
		border-radius: 20px;
		height: 120rpx;
	}

	.box4 {
		padding-top: 4%;
		padding-bottom: 4%;
		margin-top: 6%;
		margin-left: 7%;
		margin-right: 7%;
		background-color: #FFF8E5;
		display: flex;
		border-radius: 20px;
		height: 120rpx;
	}
</style>
