<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<view class="content">
			<u-search  v-model="keyword" :clearabled="false" class="searchpos" bg-color=#FFFFFF placeholder="请输入职位名称" height=77 @change="search" :show-action="false"></u-search>
		</view>
		
		<uni-fab v-if="add_able"
			:pattern="pattern"
			:popMenu=false
			@fabClick="fabClick"
			horizontal="right"
		></uni-fab>
		
		<u-modal v-model="showdelete" :content="contentdelete" @confirm="confirmdelete"  :show-confirm-button="true" :show-cancel-button="true"></u-modal>
		
		<u-swipe-action :show="item.show" :index="index"
				v-for="(item, index) in list" :key="item.jobName" 
				@click="click" @open="open"
				:options="item.jobName == empty ? options1 : options"
			>
				<view class="item u-border-bottom" @click="clickPosition(index)">
					<!-- <image mode="aspectFill" :src="images[Math.floor(Math.random() * (max - min + 1)) + min]" /> -->
					<image mode="aspectFill" :src="images[1]" />
					<text class="name">{{ item.jobName }}</text>
				</view>
				<u-gap height="25" bg-color="#F4E5E8"></u-gap>
			</u-swipe-action>
		</view>
	</view>
</template>

<script>
	import helper from '../../common/base.js'
	export default {
		data() {
			return {
				keyword:'',
				
				issearch:false,
				
				add_able:true,
				
				deleteid:'',
				showdelete:false,
				contentdelete:'确认删除此职位？',
				empty:'无',
				max:7,
				min:0,
				pattern: {
					color: 'gray',
					backgroundColor: '#FFFFFF',
					selectedColor: '#FB7897',
					buttonColor:'#FB7897'
				},
				list: [],
				images:[
					"../../static/b5.png",
					"../../static/c5.png",
					"../../static/c1.png",
					"../../static/b6.png",
					"../../static/b8.png",
					"../../static/c9.png",
					"../../static/b5.png",
					"../../static/c5.png",
					"../../static/c5.png"
				],
				options: [
					{
						text: '修改',
						style: {
							backgroundColor: '#FB7897'
						}
					},
					{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}
				],
				options1: [
					{
						text: '修改',
						style: {
							backgroundColor: '#FB7897'
						}
					},
				]
			}
		},
		onBackPress(){
			uni.reLaunch({
				url:'/pages/home/home'
			})
			return true;
		},
		onShow() {
			this.keyword='';
			if(uni.getStorageSync('global_status')=="0"){
				this.options=[];
				this.add_able=false;
			}
			this.list =uni.getStorageSync('global_job_list');
		},
		methods: {
			search(data){
				this.issearch = false;
				console.log("要搜索的职位："+data);
				if (data){
					uni.request({
						url:helper.websiteUrl+'/job/search',
						method:'POST',
						data:{
							'jobName':data
						},
						heads : {'content-type' : 'application/x-www-form-urlencoded'},
						header: {
							"token": uni.getStorageSync('token')
						},
						success: (res) => {
							console.log(res.data.code);
							if (res.data.code == 200){
								this.list = res.data.data;
								console.log(res.data.data);
								// this.$refs.uToast.show({
								// 	title: '查找职位成功',
								// 	type: 'success'
								// })
								this.issearch = true;
							}
							else{
								this.list=[];
							}
						}	
					})
				}
				else{
					this.list=uni.getStorageSync('global_job_list');
					this.issearch = true;
				}
			},
			searcherror(){
				console.log("error");
				console.log(this.issearch);
				if (this.issearch == false){
					this.$refs.uToast.show({
						title: '查找职位失败',
						type: 'error'
					})
				}
			},
			click(index, index1) {
				if (index1 == 1) {
					this.showdelete = true;
					this.deleteid = index;
				} 
				else {
					uni.setStorage({
						key:'clickPositionbox',
						data:this.list[index],
						success:(res)=>{
							console.log('存入职位信息成功');
						}
					});
					uni.navigateTo({
						url:'../editposition/editposition'
					})
					this.list[index].show = false;
				}
			},
			confirmdelete(){
				uni.request({
					url: helper.websiteUrl+'/job/delete',
					data: {
						"jobName":this.list[this.deleteid].jobName,
						"jobRemark":this.list[this.deleteid].jobRemark
					},
					method: 'POST',
					heads: {
						'content-type': 'application/x-www-form-urlencoded'
					},
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						if (res.data.code == 200) {
							this.$refs.uToast.show({
								title: '删除职位成功',
								type: 'success'
							})
							console.log("删除职位成功");
							this.list.splice(this.deleteid, 1);
							
							uni.request({
								url: helper.websiteUrl+'/job/getAll',
								data: {},
								method: 'GET',
								header: {
									"token": uni.getStorageSync('token')
								},
								success: (res) => {
									if (res.data.code == 200) {
										uni.setStorageSync('global_job_list',res.data.data);
									} else {
										this.$refs.uToast.show({
											title: '获取职位信息失败',
											type: 'error'
										})
									}
								}
							});
							
						} 
						else {
							this.$refs.uToast.show({
								title: '删除职位失败',
								type: 'error'
							})
						}
					}
				})
			},
			// 如果打开一个的时候，不需要关闭其他，则无需实现本方法
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				this.list[index].show = true;
				this.list.map((val, idx) => {
					if(index != idx) this.list[idx].show = false;
				})
			},
			fabClick(){
				uni.navigateTo({
					url:'/pages/addposition/addposition'
				})
			},
			clickPosition(index){
				uni.setStorage({
					key:'clickPosition',
					data:this.list[index],
					success:(res)=>{
						console.log('存入职位信息成功');
					}
				});
				uni.navigateTo({
					url:'/pages/positiondetail/positiondetail'
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.searchpos{
		margin-top: 20px;
	}
	
	.content{
		background-color: #F4E5E8;
		height: 60px;
	}
	
	.item {
		display: flex;
		padding: 20rpx;
		height: 88px;
	}
	
	image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		margin-right: 20rpx;
		border-radius: 12rpx;
	}
	
	.title {
		text-align: left;
		font-size: 28rpx;
		color: $u-content-color;
		margin-top: 20rpx;
	}
	
	.name {
		text-align: left;
		font-size: 19px;
		color: #000000;
		font-weight: 700;
		text-shadow: 0.5px 0.5px #778899; 
		margin-top: 15px;
		margin-left: 10px;
	}
	
	.search{
		height: 50px;
		width: 50px;
		margin-top: 5rpx;
		margin-left: 80%;
	}
	
	.vertical{
		display: flex;
		flex-direction: column;
	}
	
	.fontgap{
		font-size: 20px;
		color: #000000;
		font-weight: 700;
		text-shadow: 1px 1px #778899; 
		position: absolute;
		margin-left: 190px;
	}
</style>
