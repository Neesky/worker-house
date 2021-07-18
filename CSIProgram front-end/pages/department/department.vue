<template>
	<view>
		<view>
			<u-toast ref="uToast" />
		</view>
		
		<!-- 部门搜索 -->
		<view class="content">
			<u-search v-model="keyword" :clearabled="false" class="searchpos" bg-color=#FFFFFF placeholder="请输入部门名称" height=77 @change="search"  :show-action="false"></u-search>
			
		</view>
		
		<!-- 悬浮按钮 -->
		<uni-fab v-if="add_able"
			:pattern="pattern"
			:popMenu=false
			@fabClick="fabClick"
			horizontal="right"
		></uni-fab>
		
		<!-- 是否删除模态框 -->
		<u-modal v-model="showdelete" :content="contentdelete" @confirm="confirmdelete" :show-confirm-button="true" :show-cancel-button="true" ></u-modal>
		
		
		
		<!-- 部门列表 可右划 -->
		<u-swipe-action :show="item.show" :index="index"
				v-for="(item, index) in list" :key="item.departmentName"
				@click="click" @open="open"
				:options="item.departmentName == empty ? options1 : options"
			>
				<view class="item u-border-bottom" @click="clickbranch(index)">
					<!-- 随机icon -->
					<!-- <image mode="aspectFill" :src="images[Math.floor(Math.random() * (max - min + 1)) + min]" /> -->
					<image mode="aspectFill" :src="images[1]" />
					<text class="name">{{ item.departmentName }}</text>
				</view>
				<!-- 插入间隔槽 -->
				<u-gap height="25" bg-color="#E9E4FE"></u-gap>
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
				//悬浮按钮是否可用，管理员界面显示，用户界面禁用
				add_able:true, 
				
				deleteid:'', //删除的部门在列表的索引
				showdelete:false, //是否显示删除模态框
				contentdelete:'确认删除此部门？', //删除模态框文字
				
				issearch:false, //部门是否能搜索到
				
				empty:"无",
				max:8,
				min:0,
				pattern: { //悬浮按钮样式
					color: 'gray',
					backgroundColor: '#FFFFFF',
					selectedColor: '#A994FB',
					buttonColor:'#A994FB'
				},
				list: [], //部门列表
				images:[   //icon列表
					"../../static/b1.png",
					"../../static/branch.png",
					"../../static/b8.png",
					"../../static/b9.png",
					"../../static/b2.png",
					"../../static/b5.png",
					"../../static/b6.png",
					"../../static/b4.png",
					"../../static/b7.png",
					"../../static/b3.png"
				],
				options: [ //u-swipe-action右滑显示样式
					{
						text: '修改',
						style: {
							backgroundColor: '#A994FB'
						}
					},
					{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}
				],
				options1: [ //u-swipe-action右滑显示样式
					{
						text: '修改',
						style: {
							backgroundColor: '#A994FB'
						}
					}
				]
			}
		},
		
		//自定义返回键
		onBackPress(){
			uni.reLaunch({
				url:'/pages/home/home'
			})
			return true;
		},
		
		onShow() {
			this.keyword='';
			//取出缓存数据，global_status代表用户状态：管理员或普通用户
			//若为普通用户禁用添加按钮、删除修改操作
			if(uni.getStorageSync('global_status')=="0"){
				this.options=[];
				this.add_able=false;
			}
			this.list = uni.getStorageSync('global_department_list');
		},
		
		methods: {
			//change事件：搜索部门，支持模糊搜索
			search(data){
				this.issearch = false;
				console.log("要搜索的部门："+data);
				//数据不为空
				if (data){
					uni.request({
						url:helper.websiteUrl+'/department/search',
						method:'POST',
						data:{
							"departmentName":data
						},
						header: {
							"token": uni.getStorageSync('token')
						},
						heads : {'content-type' : 'application/x-www-form-urlencoded'},
						success: (res) => {
							if (res.data.code == 200){
								this.list = res.data.data;
								console.log(res.data.data);
								this.issearch = true;  //搜索成功
							}else{
								this.list =[];
							}
						}	
					})
				}
				//若搜索栏数据为空，呈现所有部门信息
				else{
					this.list = uni.getStorageSync('global_department_list');
				}
			},
			//search事件：点击搜索字样时触发的事件，当部门未搜索成功时，此时才弹出“查找部门失败”
			searcherror(){
				if (this.issearch == false){
					this.$refs.uToast.show({
						title: '查找部门失败',
						type: 'error'
					})
				}
			},
			
			//右滑点击修改或删除操作时触发click事件
			click(index, index1) { //index是列表索引，index1是何种操作
				//index1为1是删除操作
				if (index1 == 1) {
					this.showdelete = true; //弹出删除模态框
					this.deleteid = index;  //赋值删除索引，以便在弹出模态框后在列表中再删除该对应项
				} 
				//修改
				else {
					this.list[index].show = false; 
					uni.setStorage({  //将点击部门的信息存入本地缓存,以便下一个页面呈现
						key:'clickDepartment',
						data:this.list[index],
						success:(res)=>{
							console.log('存入部门信息成功');
						}
					});
					uni.navigateTo({ 
						url:'../editdepartment/editdepartment' //跳转到修改部门页面
					})
				}
			},
			
			//模态框确认删除
			confirmdelete(){
				uni.request({
					url: helper.websiteUrl+'/department/delete',
					data: {  //传过去部门Department类信息
						"departmentName":this.list[this.deleteid].departmentName,
						"departmentRemark":this.list[this.deleteid].departmentRemark
					},
					method: 'POST',
					heads: {
						'content-type': 'application/x-www-form-urlencoded'
					},
					header: {
						"token": uni.getStorageSync('token')
					},
					success: (res) => {
						if (res.data.code == 200) { //删除部门成功
							this.$refs.uToast.show({
								title: '删除部门成功',
								type: 'success'
							})
							console.log("删除部门成功");  
							this.list.splice(this.deleteid, 1);
							//删除成功后更新
							uni.request({
								url: helper.websiteUrl+'/department/getAll',
								data: {},
								method: 'GET',
								header: {
									"token": uni.getStorageSync('token')
								},
								success: (res) => {
									if (res.data.code == 200) {
										uni.setStorageSync('global_department_list',res.data.data);
									} else {
										this.$refs.uToast.show({
											title: '获取部门信息失败',
											type: 'error'
										})
									}
								}
							});
						} 
						else {
							this.$refs.uToast.show({  //删除部门失败
								title: '删除部门失败',
								type: 'error'
							})
						}
					}
				})
			},
			
			// 打开一个的时候，需要关闭其他
			open(index) {
				this.list[index].show = true;
				this.list.map((val, idx) => {
					if(index != idx) this.list[idx].show = false;
				})
			},
			
			//点击悬浮按钮，跳转到增加部门界面
			fabClick(){
				uni.navigateTo({
					url:'../adddepartment/adddepartment'
				})
			},
			
			//点击部门名片准备查看详情
			clickbranch(index){
				uni.setStorage({  //将点击部门的信息存入本地缓存,以便下一个页面呈现
					key:'clickBranch', 
					data:this.list[index],
					success:(res)=>{
						console.log('存入部门信息成功');
					}
				});
				uni.navigateTo({
					url:'../departmentdetail/departmentdetail' //跳转到部门详情界面
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	// 搜索栏位置
	.searchpos{
		margin-top: 20px;
	}
	
	.content{
		background-color: #ECE8FB;
		height: 60px;
	}
	
	.item {
		display: flex;
		padding: 20rpx;
		height: 88px;
	}
	
	// 图片
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
	
	//部门名称格式
	.name {
		text-align: left;
		font-size: 20px;
		color: #000000;
		font-weight: 700;
		text-shadow: 0.5px 0.5px #778899; 
		margin-top: 15px;
		margin-left: 10px;
	}
</style>
